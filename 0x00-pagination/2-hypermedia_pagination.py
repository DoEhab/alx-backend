#!/usr/bin/env python3
"""
function get_page
"""
import math
from typing import Tuple

import csv
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

    :param page: page number
    :param page_size: the number of records
    :return: tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """

        :param page: page number
        :param page_size: page size
        :return: list of result
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_ind, end_ind = index_range(page, page_size)
        result = self.dataset()
        if start_ind >= len(result):
            return []
        return result[start_ind: end_ind]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """

        :param page: page number
        :param page_size: page size
        :return: list of result
        """
        result = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": len(result),
            "page": page,
            "data": result,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
