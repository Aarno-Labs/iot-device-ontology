# tests/support/assertions.py

import jsonref
from os.path import join, dirname
from os import getcwd
from jsonschema import validate


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Loads the given schema file """

    absolute_path = join(getcwd(), filename)

    base_path = dirname(absolute_path)
    base_uri = 'file://{}/'.format(base_path)

    with open(filename) as schema_file:
        return jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)

    
