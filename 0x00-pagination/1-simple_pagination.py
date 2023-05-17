#!/usr/bin/env python3
"""Simple pagination
    Copy index_range from the previous task
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Page numbers are 1-indexed, the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
