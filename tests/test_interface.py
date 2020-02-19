# tests/test_interface.py

import json
from support.assertions import assert_valid_schema


def test_get_interface():
    with open('tests/files/test-interface.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'worldmodel/interface.json.schema')
