#!/usr/bin/env python3
'''simple pagination for API'''


from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''defining the function'''
    start_index = (page_size) * (page - 1)
    last_index = page_size * page
    # for i in range(page, page_size + 1):
    # print
    return (int(start_index), last_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''initializing the class'''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get pages and print'''
        assert type(page) == int
        assert type(page_size) == int
        try:
            ind_range = index_range(page, page_size)
            first = ind_range[0]
            last = ind_range[1]
            for page in range(first, last + 1):
                return (page)
        except IndexError:
            return []
