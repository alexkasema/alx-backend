#!/usr/bin/env python3
""" LFU caching """
from collections import defaultdict, OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching.
    This caching system uses LFU (Least Frequently Used) algorithm for caching
    If there is a tie, it uses LRU (Least Recently Used) algo to break the tie
    """
    def __init__(self):
        """ Initializing the class """
        super().__init__()
        # Keeps track of frequency of keys
        self.freq = defaultdict(int)
        # Using OrderedDict to maintain order of usage
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        If number of items in self.cache_data >= BaseCaching.MAX_ITEMS,
        Discard the least freuently used item put in the cache (LFU algorithm)
        If there is more than one item to discard, use the LRU algorithm to
        discard only the least recently used
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # update the existing key
                self.cache_data[key] = item
                self.freq[key] += 1
                self.order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # find the least frequently used key
                    least = min(self.freq.values())
                    lfu_keys = [k for k, v in self.freq.items() if v == least]

                    if len(lfu_keys) > 1:
                        # apply LRU on least frequently used keys
                        lfu_key = next(k for k in self.order if k in lfu_keys)
                    else:
                        lfu_key = lfu_keys[0]

                    del self.cache_data[lfu_key]
                    del self.freq[lfu_key]
                    del self.order[lfu_key]
                    print("DISCARD: {}".format(lfu_key))

                # Add the new key
                self.cache_data[key] = item
                self.freq[key] = 1
                self.order[key] = None

    def get(self, key):
        """ Retieve an item from the cache by its key """
        if key is None or key not in self.cache_data:
            return None

        # Increase the frequency and update the usage order
        self.freq[key] += 1
        self.order.move_to_end(key)

        return self.cache_data[key]
