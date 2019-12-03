# tests/test_device.py

import json
from support.assertions import assert_valid_schema


def test_get_device():
    with open('tests/files/test-device.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'device.json.schema')
