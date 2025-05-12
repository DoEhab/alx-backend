#!/usr/bin/env python3
"""
function get_page
"""
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
