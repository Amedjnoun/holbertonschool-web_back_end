#!/usr/bin/env python3
"""Module containing a type-annotated floor function"""
import math


def floor(n: float) -> int:
    """Return the floor of the float n

    Args:
        n (float): number to floor

    Returns:
        int: floor of n
    """
    return math.floor(n)
