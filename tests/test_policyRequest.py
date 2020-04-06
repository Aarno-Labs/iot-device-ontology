# tests/test_policyRequest.py

import json
from support.assertions import assert_valid_schema


def test_get_policyRequest():
    with open('tests/files/test-policyRequest.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/policyRequest.json.schema')
