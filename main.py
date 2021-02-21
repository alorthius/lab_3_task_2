"""
"""
import json
from pprint import pprint


def read_file(path: str):
    if not isinstance(path, str):
        return None

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

