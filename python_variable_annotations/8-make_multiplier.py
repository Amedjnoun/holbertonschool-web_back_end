#!/usr/bin/env python3
"""Module containing a type-annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier

    Args:
        multiplier (float): value to multiply by

    Returns:
        Callable[[float], float]: takes a float and returns a float
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
