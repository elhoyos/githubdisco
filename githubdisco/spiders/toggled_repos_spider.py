import os
import scrapy
import json
import re
import base64
from string import Template
from tracesets import TRACESETS, traces_in_template, regexps
from matchers import MATCHERS
from scrapy.shell import inspect_response

# Find toggled repositories via GitHub v3 API
#
# Usage:
# $ AUTH_TOKEN=... scrapy crawl toggled_repos -o ../results/normalized/results-github-scraper-`date -u "+%Y%m%d%H%M%S"`.csv

class ToggledReposSpider(scrapy.Spider):
    name = "toggled_repos"

    csv_fieldnames = ['repo_name', 'path', 'language', 'size_bytes', 'library', 'library_language', 'last_commit_ts', 'forked_from']

    headers = {
        'Authorization': 'Bearer ' + os.environ['AUTH_TOKEN'],
    }

    tracesets = TRACESETS
    matchers = MATCHERS

    search_template = 'https://api.github.com/search/code?${params}&page=${page}&per_page=${per_page}&sort=indexed&order=desc'
    per_page = 100
    max_results = 1000
    min_filesize = 0
    max_filesize = int(100e6) # https://help.github.com/en/github/managing-large-files/what-is-my-disk-quota

    def as_params(self, search_string, file_descriptors, descriptors_type):
        params_template = Template("q=${search_string}+in:file+${extensions_or_filenames}+size:${start}..${end}")

        return params_template.substitute({
            'search_string': '%22' + search_string + '%22',
            'extensions_or_filenames': '+'.join(['%s:%s' %(descriptors_type, fd) for fd in file_descriptors]),
            'start': self.min_filesize,
            'end': self.max_filesize
        })

    def search_urls(self, library, page=1):
        for traceset in self.tracesets:
            for matcher in self.matchers.get(traceset.get('lang_family')):
                file_descriptors = matcher.get('file_descriptors')
                descriptors_type = matcher.get('descriptors_type')
                template = matcher.get('template')
                self.logger.debug(traceset.get('library'))
                for traceset_value in traces_in_template(traceset, template):
                    url_template = Template(self.search_template)
                    yield (
                        url_template.substitute({
                            'params': self.as_params(traceset_value, file_descriptors, descriptors_type),
                            'page': page,
                            'per_page': self.per_page
                        }),
                        file_descriptors
                    )

    def start_requests(self):
        for traceset in self.tracesets:
            traceset['matched'] = {} # Track to avoid unnecessary requests
            for url, file_descriptors in self.search_urls(traceset):
                yield scrapy.Request(url=url, headers=self.headers, callback=self.parse, meta={ 'traceset': traceset, 'file_descriptors': file_descriptors, 'page': 1 })

    def bisect_by_filesize(self, url):
        """
        Returns a tuple with two urls with the same query but different filesize ranges.
        The page is reset to one.
        """

        size_regexp = r'size:(?P<start>\d+)..(?P<end>\d+)'
        match = re.search(size_regexp, url)
        # A match must be present, if not fail hard
        start, end = (int(size) for size in match.groups((self.min_filesize, self.max_filesize)))
        mid = int((int(end) - int(start)) / 2)
        ranges = {
            'pre': (start, mid) if mid > start else None,
            'pos': (mid + 1, end) if mid + 1 < end else None
        }

        first_page_url = re.sub(r'&page=\d+', '&page=1', url)

        return (
            re.sub(size_regexp, 'size:{0[0]}..{0[1]}'.format(ranges['pre']), first_page_url) if ranges['pre'] else None,
            re.sub(size_regexp, 'size:{0[0]}..{0[1]}'.format(ranges['pos']), first_page_url) if ranges['pos'] else None
        )

    def get_split_requests(self, response):
        start_url, end_url = self.bisect_by_filesize(response.url)
        yield response.follow(start_url, headers=self.headers, callback=self.parse, meta=response.meta) if start_url else None
        yield response.follow(end_url, headers=self.headers, callback=self.parse, meta=response.meta) if end_url else None

    def get_content_requests(self, response, items):
        for match in items:
            response.meta['repo_name'] = match['repository']['full_name']
            response.meta['path'] = match['path']
            url = match['git_url']
            yield response.follow(url, headers=self.headers, callback=self.parse_contents, meta=response.meta)

    def get_next_page_request(self, page, response):
        response.meta['page'] += 1
        next_page_url = response.url.replace('&page=' + str(page), '&page=' + str(response.meta['page']))
        return response.follow(next_page_url, headers=self.headers, callback=self.parse, meta=response.meta)

    def parse(self, response):
        page = response.meta['page']
        json_response = json.loads(response.text)

        if len(json_response['items']) > 0:
            for content_request in self.get_content_requests(response, json_response['items']):
                yield content_request

            yield self.get_next_page_request(page, response)
        elif page == 1:
            self.logger.warn('!! Found no matches for %s', response.url)

        # Try harder and lookup beyond the limits
        if json_response['total_count'] > self.max_results:
            self.logger.info('Split for %s', response.url)
            for split_request in self.get_split_requests(response):
                yield split_request
        elif json_response['incomplete_results']:
            self.logger.info('Incomplete results for %s', response.url)
            for split_request in self.get_split_requests(response):
                yield split_request

    # TODO: augment here, optionally
    def parse_contents(self, response):
        matched = response.meta['traceset']['matched']
        repo_name = response.meta['repo_name']
        if matched.get(repo_name):
            return

        path = response.meta['path']
        json_response = json.loads(response.text)
        # Some files will arrive as non utf-8 (specially txt files), let's ignore,
        # the output seems to be ok for our purposes
        content = str(base64.b64decode(json_response['content']), encoding='utf-8', errors='ignore')

        traceset = response.meta['traceset']
        library = traceset.get('library')
        lang_family = traceset.get('lang_family')
        file_descriptors = response.meta['file_descriptors']
        for regexp in regexps(traceset, file_descriptors):
            if matched.get(repo_name):
                break

            self.logger.debug('Search %s in %s', regexp, path)
            
            if re.search(regexp, content):
                matched[repo_name] = True
                self.logger.info('Matched %s in %s', library, repo_name)
                toggled_repo = { key: None for key in self.csv_fieldnames }
                toggled_repo['repo_name'] = repo_name
                toggled_repo['path'] = path
                toggled_repo['library'] = library
                toggled_repo['library_language'] = lang_family
                yield toggled_repo

