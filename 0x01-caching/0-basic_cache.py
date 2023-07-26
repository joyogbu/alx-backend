#!/usr/bin/env python3
'''BasicCache that inherits from BaseCaching and is a caching'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class that inherits from BaseCaching'''

    def __init__(self):
        '''defining the class'''
        super().__init__()
        self.my_dict = self.cache_data

    def put(self, key, item):
        '''defining the function'''
        if key is None or item is None:
            pass
        else:
            self.my_dict[key] = item

    def get(self, key):
        '''defining the function'''
        if key is None:
            return None
        try:
            return self.my_dict[key]
        except KeyError:
            return None
