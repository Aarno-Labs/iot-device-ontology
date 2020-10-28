# tests/test_appliedOnHostAction.py
import json
from support.assertions import assert_valid_schema


def test_get_appliedOnHostAction():
    with open('tests/files/test-fingerprint.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'operations/fingerprint.json.schema')
