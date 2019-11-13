# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.repos_seen = set()

    def process_item(self, item, spider):
        if spider.name not in ['toggled_repos']:
            return item

        key = '{repo_name}_{path}'.format(**item)
        if key in self.repos_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.repos_seen.add(key)
            return item
