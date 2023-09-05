#!/usr/bin/python3

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                #Discard the last item (LIFO)
                last_key = list(self.cache_data.keys())[-1]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]
            self.cache_data[key] = item

        def get(self, key):
            if key is not None:
                return self.cache_data.get(key, None)
            else:
                return None
