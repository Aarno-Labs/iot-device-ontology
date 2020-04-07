# tests/test_agentSpawnEvent.py

import json
from support.assertions import assert_valid_schema


def test_get_agentSpawnEvent():
    with open('tests/files/test-fingerprintdata-hikeresponse.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'ta3-c2/fingerprintData.json.schema')

def test_get_agentSpawnEvent_noTimestamp():
    with open('tests/files/test-fingerprintdata-fingerprint.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                             'ta3-c2/fingerprintData.json.schema')
