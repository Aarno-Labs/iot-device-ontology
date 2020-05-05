# tests/test_network-based.py

import json
from support.assertions import assert_valid_schema


def test_get_network_based():
    with open('tests/files/test_network-based.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'operations/neutralization.json.schema')

def test_get_file_based():        
    with open('tests/files/test_file-based.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'operations/neutralization.json.schema')
