#!/usr/bin/python3

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = [] # To maintain the order of item access(i.e to keep track of the way keys where accessed, most recently used are at the end of the list and least recently used are at the beginning 

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                #Discard the least recently used item in cache(LRU)
                self.evict_lru()
            self.cache_data[key] = item
            self.order.append(key) # Add key to the order list


    def get(self, key):
            if key is not None:
                if key in self.cache_data:
                    if key in self.order: #if the key exists in the ordered list then
                        self.order.remove(key) # reomve the key from its current location in the orderedlist
                    self.order.append(key) # add the key to the end of the list as the the MRU
                    return self.cache_data.get(key, None)
            else:
                return None

    def evict_lru(self):
        if self.order:
            lru_key = self.order.pop(0) # remove the first key (which is the LRU)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
