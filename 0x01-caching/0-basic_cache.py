#!/usr/bin/env python3
'''BasicCache that inherits from BaseCaching and is a caching'''


from base_caching import BaseCaching
'''class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in\
                your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in\
                your cache class")'''


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
        self.my_dict[key] = item

    def get(self, key):
        '''defining the function'''
        # if key or key is not None:
        try:
            return self.my_dict[key]
        except KeyError:
            return None
