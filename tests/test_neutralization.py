# tests/test_network-based.py

import json
from support.assertions import assert_valid_schema, assert_invalid_schema


def test_get_network_based():
    with open('tests/files/test_network-based.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'operations/neutralization.json.schema')

def test_get_file_based():
    valid_files = ['tests/files/test_file-based.json',
                   'tests/files/test_file-based-1.json',
                   'tests/files/test_file-based-2.json',
                   'tests/files/test_file-based-5.json',]

    for f in valid_files: 
        with open(f) as json_file:
            json_data = json.load(json_file)
            assert_valid_schema(json_data, 'operations/neutralization.json.schema')


    invalid_files = ['tests/files/test_file-based-3.json',
                     'tests/files/test_file-based-4.json']

    for f in invalid_files: 
        with open(f) as json_file:
            json_data = json.load(json_file)
            assert_invalid_schema(json_data, 'operations/neutralization.json.schema')

