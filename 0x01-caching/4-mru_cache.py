#!/usr/bin/python3

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = [] # To maintain the order of item access(i.e to keep track of the way keys where accessed, most recently used are at the end of the list and least recently used are at the beginning 

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                #Discard the Most recently used item in cache(MRU)
                self.evict_mru()
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

    def evict_mru(self):
        if self.order:
            mru_key = self.order[-1] # remove the last key (which is the MRU)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
