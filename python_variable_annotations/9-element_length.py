#!/usr/bin/env python3
"""Module containing a type-annotated element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their length

    Args:
        lst (Iterable[Sequence]): iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: list of tuples with sequence and length
    """
    return [(i, len(i)) for i in lst]
