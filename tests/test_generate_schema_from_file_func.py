import pytest
from solution import generate_schema_from_file


def test_input_with_non_existing_file():
    result = generate_schema_from_file('no_file.json', 'result_data')
    assert result is None


def test_input_without_message_attribute(raw_data_3_file):
    result = generate_schema_from_file(raw_data_3_file, 'result_data')
    assert result is None


def test_input_with_message_attribute(raw_data_2_file):
    result_file = "schema/test_result.json"
    result = generate_schema_from_file(raw_data_2_file, 'test_result')
    assert type(result) == str
    assert result == result_file
