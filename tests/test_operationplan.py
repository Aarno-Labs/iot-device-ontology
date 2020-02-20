# tests/test_operationplan.py

import json
from support.assertions import assert_valid_schema


def test_get_operationplan():
    with open('tests/files/test-operationplan.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'operations/operationplan.json.schema')
