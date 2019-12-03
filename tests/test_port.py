# tests/test_port.py

import json
from support.assertions import assert_valid_schema


def test_get_port():
    with open('tests/files/test-port.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'port.json.schema')
