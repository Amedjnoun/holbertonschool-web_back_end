# Pagination

## Description
This project focuses on implementing different pagination strategies for API endpoints. Pagination is a technique used to divide large datasets into smaller, manageable chunks or pages to improve performance and user experience.

## Learning Objectives
By the end of this project, you should be able to explain:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5.*)
- All modules should have documentation
- All functions should have documentation
- All functions and coroutines must be type-annotated

## Setup
Use the provided `Popular_Baby_Names.csv` data file for the project.

## Tasks

### 0. Simple helper function
- Implement a function named `index_range` that takes two integer arguments `page` and `page_size`
- The function should return a tuple of size two containing a start index and an end index
- These indexes correspond to the range of indexes to return in a list for those pagination parameters
- Page numbers are 1-indexed (first page is page 1)

### 1. Simple pagination
- Implement a `Server` class with a method `get_page`
- The method takes two integer arguments: `page` (default 1) and `page_size` (default 10)
- Use the provided CSV file to populate the dataset
- Verify that both arguments are integers greater than 0
- Use the `index_range` function to paginate the dataset correctly
- Return the appropriate page of the dataset

### 2. Hypermedia pagination
- Implement a `get_hyper` method that extends the functionality of `get_page`
- Return a dictionary containing key-value pairs with pagination metadata:
  - `page_size`: length of the returned dataset page
  - `page`: current page number
  - `data`: the dataset page
  - `next_page`: number of the next page, None if no next page
  - `prev_page`: number of the previous page, None if no previous page
  - `total_pages`: total number of pages in the dataset

### 3. Deletion-resilient hypermedia pagination
- Implement a `get_hyper_index` method that handles pagination even when items are deleted
- Return a dictionary with the following key-value pairs:
  - `index`: current start index of the page
  - `next_index`: next index to query with
  - `page_size`: current page size
  - `data`: actual page of the dataset
- Ensure the method is resilient to item deletion between queries

## Files
- `0-simple_helper_function.py`: Implementation of the `index_range` function
- `1-simple_pagination.py`: Implementation of the `Server` class with `get_page` method
- `2-hypermedia_pagination.py`: Implementation of the `Server` class with `get_hyper` method
- `3-hypermedia_del_pagination.py`: Implementation of deletion-resilient pagination