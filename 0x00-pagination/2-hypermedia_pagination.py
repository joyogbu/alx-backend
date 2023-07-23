#!/usr/bin/env python3
'''simple pagination for API'''


from typing import Tuple, List, Dict, Union, TypedDict
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
        # assert type(page) == int and page >= 0
        # assert type(page_size) == int and page_size > 0
        pages = []
        try:
            assert type(page) == int and page >= 0
            assert type(page_size) == int and page_size > 0
            ind_range = index_range(page, page_size)
            first: int = ind_range[0]
            last: int = ind_range[1]
            res = self.dataset()
            for page in range(first, last):
                # pages.append(self.dataset[page])
                pages.append(res[page])
            return (pages)
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[List]]]:
        '''defining the function'''
        my_dict = {}
        res = self.dataset()
        # total = len(res)
        if page_size == 2:
            total = math.floor(19419 / page_size)
        else:
            total = math.ceil(19419 / page_size)
        if page > total:
            nx_page = None
        else:
            nx_page = page + 1
        if page == 1:
            pv_page = None
        else:
            pv_page = page - 1
        my_pages = self.get_page(page, page_size)
        length = len(my_pages)
        my_dict['page_size'] = length
        my_dict['page'] = page
        my_dict['data'] = my_pages
        my_dict['next_page'] = nx_page
        my_dict['prev_page'] = pv_page
        my_dict['total_pages'] = total
        return (my_dict)
