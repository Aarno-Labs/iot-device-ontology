# tests/test_newC2Event.py

import json
from support.assertions import assert_valid_schema


def test_get_newC2():
    with open('tests/files/test-newC2Event.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/newC2Event.json.schema')
