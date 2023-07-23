#!/usr/bin/env python3
'''simple helper function that rerurns a tuple'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''defining the function'''
    start_index = (page_size / page) * (page - 1)
    last_index = page_size * page
    # for i in range(page, page_size + 1):
    # print
    return (int(start_index), last_index)
