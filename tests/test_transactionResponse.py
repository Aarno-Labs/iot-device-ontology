# tests/test_transactionResponse.py

import json
from support.assertions import assert_valid_schema


def test_get_transactionResponse():
    with open('tests/files/test-transactionResponse.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/transactionResponse.json.schema')
