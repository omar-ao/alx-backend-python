#!/usr/bin/env python3
"""This is `9-element_length.py` module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list"""
    return [(i, len(i)) for i in lst]
