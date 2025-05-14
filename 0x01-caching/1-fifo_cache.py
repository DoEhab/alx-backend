#!/usr/bin/python3
"""
FIFOCache module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    first in first out cache inherit from base caching
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
        return self.cache_data[key]
