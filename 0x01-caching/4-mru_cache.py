#!/usr/bin/env python3
""" MRU caching """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching.
    This caching system uses MRU (Most Recently Used) algorithm for caching
    """
    def __init__(self):
        """ Initializing the class """
        super().__init__()
        # Using OrderedDict to maintain order of insertion and access
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        If number of items in self.cache_data >= BaseCaching.MAX_ITEMS,
        Discard the most recently used item put in the cache (MRU algorithm)
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent_key = next(reversed(self.cache_data))
                del self.cache_data[most_recent_key]
                print("DISCARD: {}".format(most_recent_key))

            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ Retieve an item from the cache by its key """
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data.pop(key)
        # Reinsert to amrk as recently used
        self.cache_data[key] = item

        return item
