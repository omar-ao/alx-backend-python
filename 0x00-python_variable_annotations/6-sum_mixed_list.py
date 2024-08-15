#!/usr/bin/env python3
"""This is `6-sum_mixed_list.py` module"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the elements fo mxd_lst"""
    sum: float = 0
    for n in mxd_lst:
        sum = sum + n
    return sum
