import jsonref
import json
import sys
from os.path import join, dirname
from os import getcwd
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

### Validate stdin json against arg1 json schema file ###

def usage():
    print("JSON-Schema Validator: validate json file from stdin against schema.")
    print("    usage: {} SCHEMA_FILE.json".format(sys.argv[0]))

def load_json_schema(filename):
    """ Loads the given schema file """

    absolute_path = join(getcwd(), filename)

    base_path = dirname(absolute_path)
    base_uri = 'file://{}/'.format(base_path)

    try:
        with open(filename) as schema_file:
            return jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)
    except IOError as x:
        print("Error: Could not open or parse schema file (arg 1):", x)
        usage()
        sys.exit(1)
    
def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = load_json_schema(schema_file)
    try:
        validate(data, schema)
    except ValidationError as e:
        print("Validation error: {}".format(e.message))
        sys.exit(1)

def main():
    # This expects a schema file as an argument, and the json file
    # in stdin

    if len(sys.argv) != 2:
        print("Error: Exactly one schema file required.")
        usage()
        sys.exit(1)
          
    # read json string from stdin
    json_str = sys.stdin.read()
    # validate it is valid json
    try:
        json_data = json.loads(json_str)
    except ValueError as err:
        print("Error parsing json: ", err)
        sys.exit(1)

    assert_valid_schema(json_data, sys.argv[1])
        
    sys.exit(0)
    
if __name__== "__main__":
  main()
