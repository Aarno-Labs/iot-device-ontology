# tests/test_eventWrapper.py

import json
from support.assertions import assert_valid_schema


def test_get_eventWrapper():
    with open('tests/files/test-eventWrapper.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/eventWrapper.json.schema')
