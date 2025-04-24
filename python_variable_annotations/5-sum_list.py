#!/usr/bin/env python3
"""Module containing a type-annotated sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats

    Args:
        input_list (List[float]): list of floats to sum

    Returns:
        float: sum of all values in the list
    """
    return sum(input_list)
