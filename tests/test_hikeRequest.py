# tests/test_hikeRequest.py

import json
from support.assertions import assert_valid_schema


def test_get_network_based():
    with open('tests/files/test_hikeRequest.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'fingerprint/hike-request.json.schema')

def test_get_bot_detection():
    with open('tests/files/test_hikeRequest-bot.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'fingerprint/hike-request.json.schema')
        
