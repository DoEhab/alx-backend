#!/usr/bin/python3
"""
LIFOCache module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least recently used cache
    """

    def __init__(self):

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """

        :param key: dictionary key
        :param item: dictionary item
        :return: none
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key, _ = self.cache_data.popitem(last=False)
                    print("DISCARD:", oldest_key)
                self.cache_data[key] = item

    def get(self, key):
        """

        :param key: dictionary key
        :return: the value
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
