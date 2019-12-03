# tests/test_host.py

import json
from support.assertions import assert_valid_schema


def test_get_host():
    with open('tests/files/test-host.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'host.json.schema')
