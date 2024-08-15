#!/usr/bin/env python3
"""This is the `8-make_multiplier.py` module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a functions that multiplies multiplier by its argument"""
    def F(b: float) -> float:
        return multiplier * b
    return F
