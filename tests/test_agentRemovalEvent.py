# tests/test_agentRemovalEvent.py

import json
from support.assertions import assert_valid_schema


def test_get_agentRemovalEvent():
    with open('tests/files/test-agentRemovalEvent.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'hike-mgt-api/agentRemovalEvent.json.schema')
