import pytest
from solution import map_field
from solution import FieldType


def test_str_fields(fetch_data1):
    result = map_field(fetch_data1['battle']['id'])
    assert type(result) == dict
    assert result['type'] == FieldType.STRING
    assert 'tag' in result
    assert 'description' in result
    assert result['required'] is False


def test_integer_fields(fetch_data2):
    result = map_field(fetch_data2['time'])
    assert type(result) == dict
    assert result['type'] == FieldType.INTEGER


def test_boolean_fields(fetch_data2):
    result = map_field(fetch_data2['publicFeed'])
    assert result['type'] == FieldType.BOOLEAN


def test_string_array_fields(fetch_data2):
    result = map_field(fetch_data2['internationalCountries'])
    assert result['type'] == FieldType.ENUM


def test_object_array_fields(fetch_data1):
    result = map_field(fetch_data1['battle']['participants'])
    assert type(result) == dict
    assert result['type'] == FieldType.ARRAY
    assert 'items' in result


def test_object_fields(fetch_data2):
    result = map_field(fetch_data2['user'])
    assert type(result) == dict
    assert result['type'] == FieldType.OBJECT
    assert 'schema' in result
    assert type(result['schema']) == dict
