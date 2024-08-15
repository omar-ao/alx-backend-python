#!/usr/bin/env python3
"""This is `5-sum_list.py` module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This returns the sum of the input_list"""
    sum: float = 0
    for num in input_list:
        sum = sum + num
    return sum
