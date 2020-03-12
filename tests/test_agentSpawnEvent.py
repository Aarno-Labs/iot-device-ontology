# tests/test_agentSpawnEvent.py

import json
from support.assertions import assert_valid_schema


def test_get_agentSpawnEvent():
    with open('tests/files/test-agentSpawnEvent.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/agentSpawnEvent.json.schema')
