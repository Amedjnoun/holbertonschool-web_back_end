#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with the following key-value pairs:
        - index: the current start index of the return page
        - next_index: the next index to query with
        - page_size: the current page size
        - data: the actual page of the dataset

        Args:
            index (int, optional): The starting index. Defaults to 0.
            page_size (int, optional): The page size. Defaults to 10.

        Returns:
            Dict: Dictionary containing pagination information
        """
        # Set default index to 0 if None
        if index is None:
            index = 0

        # Get indexed dataset
        indexed_dataset = self.indexed_dataset()
        dataset_size = len(indexed_dataset)

        # Assert index is in valid range
        assert isinstance(index, int) and 0 <= index < dataset_size

        # Collect data for the current page
        data = []
        current_index = index

        # Find the next index where data exists
        while len(data) < page_size and current_index < dataset_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        # Find the next index to query
        next_index = current_index

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
