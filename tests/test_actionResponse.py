# tests/test_actionResponse.py

import json
from support.assertions import assert_valid_schema


def test_get_network_based():
    with open('tests/files/test_actionresponse.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data, 'rfc-messages/action-response.json.schema')
