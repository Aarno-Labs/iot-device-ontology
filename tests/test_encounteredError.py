# tests/test_encounteredError.py

import json
from support.assertions import assert_valid_schema


def test_get_encounteredError():
    with open('tests/files/test-encounteredError.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/encounteredError.json.schema')
