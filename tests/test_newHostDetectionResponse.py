# tests/test_newHostDetection.py

import json
from support.assertions import assert_valid_schema


def test_get_newHostDetection():
    with open('tests/files/test-newHostDetectionResponse.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(
                json_data,
                'hike-mgt-api/newHostDetectionResponse.json.schema')
