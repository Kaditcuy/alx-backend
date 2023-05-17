#!/usr/bin/env python3
"""Hypermedia pagination
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Page numbers are 1-indexed, the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
