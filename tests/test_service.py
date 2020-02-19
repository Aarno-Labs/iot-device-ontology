# tests/test_serviceVersion.py

import json
from support.assertions import assert_valid_schema


def test_get_service():
    with open('tests/files/test-service.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'worldmodel/service.json.schema')
