#!/usr/bin/env python3
"""This is the `7-to_kv.py' module"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v ** 2)
