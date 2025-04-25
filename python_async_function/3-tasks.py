#!/usr/bin/env python3
"""Module that returns an asyncio.Task"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
