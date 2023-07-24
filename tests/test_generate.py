#!/usr/bin/env python3
import pytest
import os
from gendiff.generate_diff import generate_diff
from tests.fixtures.right_answer import right_answer

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file1_yml = 'tests/fixtures/file1.yml'
file2_yml = 'tests/fixtures/file2.yml'


#right_answer = open('tests/fixtures/right_answer.txt', 'r')


def test_generate_diff():
    assert generate_diff(file1_json, file2_json) == right_answer
    assert generate_diff(file1_yaml, file2_yaml) == right_answer
    assert generate_diff(file1_yml, file2_yml) == right_answer


def test_type_test_generate_diff():
    text = 'text'
    assert type(generate_diff(file1_json, file2_json)) == type(text)
    assert type(generate_diff(file1_yaml, file2_yaml)) == type(text)
    assert type(generate_diff(file1_yml, file2_yml)) == type(text)


#def len_text_test_generate_diff():
    #assert len(generate_diff(file1_json, file2_json)) == 128


def test_format():
    assert file1_json[len(file1_json)-5:len(file1_json)] == '.json'
    assert file2_json[len(file2_json)-5:len(file2_json)] == '.json'
    assert file1_yaml[len(file1_yaml)-5:len(file1_yaml)] == '.yaml'
    assert file2_yaml[len(file2_yaml)-5:len(file2_yaml)] == '.yaml'
    assert file1_yml[len(file1_yml)-4:len(file1_yml)] == '.yml'
    assert file2_yml[len(file2_yml)-4:len(file2_yml)] == '.yml'
