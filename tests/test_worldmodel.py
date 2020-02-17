# tests/test_worldmodel.py

import json
from support.assertions import assert_valid_schema


def test_get_worldmodel():
    with open('tests/files/test-worldmodel.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'worldmodel.json.schema')
