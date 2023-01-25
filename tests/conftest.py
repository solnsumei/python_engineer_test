import json

import pytest


def fetch_file_data(json_file: str) -> dict:
    with open(json_file) as f:
        data = json.load(f)
        return data['message']


@pytest.fixture
def fetch_data1():
    return fetch_file_data("data/data_1.json")


@pytest.fixture
def fetch_data2():
    return fetch_file_data("data/data_2.json")


@pytest.fixture
def fetch_result1():
    return fetch_file_data("data/result_1.json")


@pytest.fixture
def fetch_result2():
    return fetch_file_data("data/result_2.json")
