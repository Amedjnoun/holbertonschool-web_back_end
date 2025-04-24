#!/usr/bin/env python3
"""Module containing a type-annotated to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key and its value to a tuple with the square of the value

    Args:
        k (str): string key
        v (Union[int, float]): integer or float value

    Returns:
        Tuple[str, float]: tuple containing the key and the square of the value
    """
    return (k, float(v ** 2))
