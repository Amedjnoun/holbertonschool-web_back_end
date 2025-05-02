# holbertonschool-web_back_end

## Python - Async Comprehension

This project covers asynchronous programming in Python, focusing on asynchronous generators and comprehensions. You will learn how to write async generators, use async comprehensions, and type-annotate generators.

### Concepts
- Python - Asynchronous execution
- Python - Asynchronous Programming

### Resources
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#asynchronous-comprehensions-generators)
- [Type-hints for generators](https://github.com/python/typing/issues/449)

### Learning Objectives
By the end of this project, you should be able to:
- Write an asynchronous generator
- Use async comprehensions
- Type-annotate generators

### Requirements
- Python 3.9, Ubuntu 20.04 LTS
- All files must end with a new line
- First line of all Python files: `#!/usr/bin/env python3`
- Code style: pycodestyle (2.5.x)
- All modules and functions must have documentation
- All functions and coroutines must be type-annotated

### Tasks

#### 0. Async Generator
Write a coroutine `async_generator` that loops 10 times, waits 1 second each time, and yields a random number between 0 and 10.

#### 1. Async Comprehensions
Write a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator` and returns them.

#### 2. Run time for four parallel comprehensions
Write a coroutine `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`, measures the total runtime, and returns it.

---

**Directory:** `python_async_comprehension`

**Repository:** holbertonschool-web_back_end