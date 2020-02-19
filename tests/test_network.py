# tests/test_network.py

import json
from support.assertions import assert_valid_schema


def test_get_network():
    with open('tests/files/test-network.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'operations/network.json.schema')
