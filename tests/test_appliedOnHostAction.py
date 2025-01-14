# tests/test_appliedOnHostAction.py

import json
from support.assertions import assert_valid_schema


def test_get_appliedOnHostAction():
    with open('tests/files/test-appliedOnHostActionEvent.json') as json_file:
        json_data = json.load(json_file)

        assert_valid_schema(json_data,
                            'hike-mgt-api/appliedOnHostActionEvent.json.schema')
