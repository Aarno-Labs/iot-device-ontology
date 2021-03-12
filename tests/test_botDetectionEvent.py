# tests/test_botdetectionEvent.py

import json
from support.assertions import assert_valid_schema


def test_get_botDetectionEvent():
    with open('tests/files/test-botdetection-event.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/botDetectionEvent.json.schema')

