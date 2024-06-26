#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching.
    This caching system uses FIFO (First In First Out) algorithm for caching
    """
    def __init__(self):
        """ Initializing the class """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        If number of items in self.cache_data >= BaseCaching.MAX_ITEMS,
        Discard the first item put in the cache (FIFO algorithm)
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.keys_order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

            self.cache_data[key] = item
            self.keys_order.append(key)

    def get(self, key):
        """ Retieve an item from the cache by its key """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
