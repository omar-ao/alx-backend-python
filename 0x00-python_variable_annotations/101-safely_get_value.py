#!/usr/bin/env python3
"""This is the `101-safely_get_value.py` module"""
from typing import Any, Union, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'),
                     None] = None) -> Union[Any, TypeVar('T')]:
    """Returns list"""
    if key in dct:
        return dct[key]
    else:
        return default
