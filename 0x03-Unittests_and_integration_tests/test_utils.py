#!/usr/bin/env python3
"""
Test Module
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap
    """
    @parameterized.expand([
        ("test_1", {"a": 1}, ("a",), 1),
        ("test_2", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("test_3", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, name: str, a: Mapping,
                               b: Sequence, expected: Any) -> None:
        """
        test_access_nested_map
        """
        result = access_nested_map(a, b)
        self.assertEqual(result, expected)
