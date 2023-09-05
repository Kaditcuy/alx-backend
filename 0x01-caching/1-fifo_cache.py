#!/usr/bin/python3

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                #Evict the first item (FIFO)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"Discard: {first_key}")
            self.cache_data[key] = item

        def get(self, key):
            if key is not None:
                self.cache_data.get(key, None)
            else:
                return None
