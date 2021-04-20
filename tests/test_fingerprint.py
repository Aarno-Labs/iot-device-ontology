# tests/test_fingerprint.py
import json
from support.assertions import assert_valid_schema


def test_get_fingerprint0():
    with open('tests/files/test-fingerprint.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'operations/hike-fingerprint.json.schema')


def test_get_fingerprint1():
    with open('tests/files/test-fingerprint-1.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'operations/hike-fingerprint.json.schema')
