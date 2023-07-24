#!/usr/bin/env python3
from gendiff.parser_diff import parser_diff
from tests.fixtures.right_answer import right_answer

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file1_yml = 'tests/fixtures/file1.yml'
file2_yml = 'tests/fixtures/file2.yml'


def test_parser():
    assert parser_diff(file1_json) == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert parser_diff(file1_yaml) == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert parser_diff(file1_yml) == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
