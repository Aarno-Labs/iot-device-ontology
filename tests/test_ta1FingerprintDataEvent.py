# tests/test_ta1FingerprintData.py

import json
from support.assertions import assert_valid_schema


def test_get_ta1FingerprintData():
    with open('tests/files/test-ta1FingerprintData.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/ta1FingerprintDataEvent.json.schema')

