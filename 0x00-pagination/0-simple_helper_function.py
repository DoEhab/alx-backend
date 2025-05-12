#!/usr/bin/env python3
"""
function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

    :param page: page number
    :param page_size: the number of records
    :return: tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
