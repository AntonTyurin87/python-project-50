#!/usr/bin/env python3
import json
import yaml

# file = 'tests/fixtures/file2.json'
# file = 'tests/fixtures/file1.yaml'
# file = 'tests/fixtures/file1.yml'


def parser_diff(file):
    if file[len(file) - 5:len(file)] == '.json':
        return json.load(open(file))
    elif file[len(file) - 5:len(file)] == '.yaml':
        return yaml.safe_load(open(file))
    elif file[len(file) - 4:len(file)] == '.yml':
        return yaml.safe_load(open(file))

# print(parser_diff(file))
