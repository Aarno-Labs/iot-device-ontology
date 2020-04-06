# tests/test_operationPhaseUpdate.py

import json
from support.assertions import assert_valid_schema


def test_get_operationPhaseUpdate():
    with open('tests/files/test-operationPhaseUpdate.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/operationPhaseUpdate.json.schema')
