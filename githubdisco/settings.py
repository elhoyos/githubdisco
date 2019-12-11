# -*- coding: utf-8 -*-

# Scrapy settings for githubdisco project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'githubdisco'

SPIDER_MODULES = ['githubdisco.spiders']
NEWSPIDER_MODULE = 'githubdisco.spiders'

# LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'githubdisco-UNALConcordiaResearch (+http://das.encs.concordia.ca)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_FORMAT = 'csv'
FEED_EXPORT_FIELDS = None # Each spider yields to a dict with the fields
# TODO: have augmented_toggled_repos and top_contributors spiders to define their fields
# FEED_EXPORT_FIELDS = ['repo_name', 'language', 'size_bytes', 'number_of_commits', 'last_commit_ts', 'forked_from', 'number_of_contributors', 'repo_not_found', 'first_commit_sha', 'created_at'] # augmented_toggled_repos
# FEED_EXPORT_FIELDS = ['library', 'repo_name', 'login', 'name', 'email'] # top_contributors

# In some unfrequent situations a 403 is returned due to
# throttling, keep retrying until done
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 403]
RETRY_TIMES = 1000000000000

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 6 # Set to your number of tokens

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# GitHub max limit is 5000 req/hour => 0.72 sec/req
# But you do not want to delay much from it to get advantage of the concurrent
# requests.
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'githubdisco.middlewares.GithubdiscoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'githubdisco.middlewares.GithubdiscoDownloaderMiddleware': 543,
}

SPIDER_CONTRACTS = {
   'githubdisco.contracts.WithMetaContract': 10,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'githubdisco.pipelines.DuplicatesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
