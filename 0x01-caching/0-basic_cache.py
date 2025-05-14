#!/usr/bin/python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache inherits from base caching
    """

    def put(self, key, item):
        """

        :param key: dictionary key
        :param item: dictionary item
        :return: none
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """

        :param key: dictionary key
        :return: the value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
