#!/usr/bin/env python3
'''FIFOCache that inherits from BaseCaching and is a caching'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''fifocache inheriting feom basecaching'''

    def __init__(self):
        '''initializing the class'''
        super().__init__()
        self.my_dict = self.cache_data

    def put(self, key, item):
        '''defining the class'''
        length = len(self.my_dict)
        # self.my_dict[key] = item
        if key is None or item is None:
            pass
        # if key not in self.my_dict.keys():
        # self.my_dict[key] = item
        if length >= BaseCaching.MAX_ITEMS:
            key_list = list(self.my_dict.keys())
            first_key = key_list[0]
            del self.my_dict[first_key]
            print("DISCARD: {}".format(first_key), end='\n')
        self.my_dict[key] = item
        # print()

    def get(self, key):
        '''defining the function'''
        if key is None:
            return None
        try:
            return self.my_dict[key]
        except KeyError:
            return None
