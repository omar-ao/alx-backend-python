#!/usr/bin/env python3
"""This is the `100-safe_first_element.py` module"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a list or None"""
    if lst:
        return lst[0]
    else:
        return None
