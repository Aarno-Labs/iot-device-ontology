# tests/test_newActiveFingerprint.py

import json
from support.assertions import assert_valid_schema


def test_get_newActiveFingerprint():
    with open('tests/files/test-newActiveFingerprint.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/newActiveFingerprintEvent.json.schema')
