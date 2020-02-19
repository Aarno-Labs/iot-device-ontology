# tests/test_isatypeVersion.py

import json
from support.assertions import assert_valid_schema


def test_get_isatype():
    with open('tests/files/test-isatype.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'worldmodel/isatype.json.schema')
