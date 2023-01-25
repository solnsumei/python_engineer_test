# Create enum field types
import json
import os
from enum import Enum
from typing import Any


class FieldType(str, Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    ENUM = "enum"
    ARRAY = "array"
    OBJECT = "object"


def map_field(field: Any) -> dict:
    """
    Function to map fields to their respective mapped values according to the value type provided.
    :param field: Any
    :return: dict
    """
    # Create default values
    mapped_value = {
        "tag": "",
        "description": "",
        "required": False
    }
    # Creating a field_type variable to maintain consistency and avoid typo
    field_type = 'type'
    if type(field) == bool:
        mapped_value[field_type] = FieldType.BOOLEAN
    elif type(field) == str:
        mapped_value[field_type] = FieldType.STRING
    elif type(field) == int:
        mapped_value[field_type] = FieldType.INTEGER
    elif type(field) == float:
        mapped_value[field_type] = FieldType.FLOAT
    elif type(field) == list:
        if len(field) > 0:
            if type(field[0]) == str:
                mapped_value[field_type] = FieldType.ENUM
            elif type(field[0] == dict):
                mapped_value[field_type] = FieldType.ARRAY
                items_schema = {
                    field_type: FieldType.OBJECT,
                    'schema': create_schema(field[0])
                }
                mapped_value['items'] = items_schema
        else:
            mapped_value[field_type] = FieldType.ENUM
    elif type(field) == dict:
        mapped_value[field_type] = FieldType.OBJECT
        # if the dictionary(object) field has attributes, create schema for them.
        if len(field) > 0:
            # Make a recursive call to create_schema for child nodes
            mapped_value['schema'] = create_schema(field)
    return mapped_value


def create_schema(message: dict) -> dict:
    """
    Method to create schema from dictionary of fields
    :param message: dict
    :return: dict
    """
    schema = {}
    for key, value in message.items():
        schema[key] = map_field(value)
    return schema


def generate_schema_from_file(source_file: str, output_file: str) -> str | None:
    """
    Method to generate schema from json source file and saves the json schema to output file provided.
    :param source_file: str
    :param output_file: str
    :return: None
    """
    try:
        with open(source_file) as f:
            data = json.load(f)
            if 'message' not in data:
                print('No message field in data, exiting...')
                return

        # Create schema for file data
        schema = create_schema(data['message'])

        # Setup output file
        output_filename = f'schema/{output_file}.json'
        with open(output_filename, 'w') as f:
            json.dump(schema, f, indent=4)  # Using indentation to make output write on multiple lines
            print(f"Output schema generated and saved at {output_filename}")
            return output_filename
    except Exception as ex:
        print(ex)
