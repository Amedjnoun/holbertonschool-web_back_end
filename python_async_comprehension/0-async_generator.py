#!/usr/bin/env python3
"""
Async Generator module
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10
    Loop 10 times, each time asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
