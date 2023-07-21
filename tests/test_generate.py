#!/usr/bin/env python3
import pytest
import os
from gendiff.generate_diff import generate_diff
from tests.fixtures.right_answer import right_answer

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file3_false = ''

#right_answer = open('tests/fixtures/right_answer.txt', 'r')


def test_generate_diff():
    assert generate_diff(file1_json, file2_json) == right_answer


def test_generate_diff_file():
    assert generate_diff(file1_json, file3_false) == 'ancorrect file'


def test_type_test_generate_diff():
    text = 'text'
    assert type(generate_diff(file1_json, file2_json)) == type(text)


#def len_text_test_generate_diff():
    #assert len(generate_diff(file1_json, file2_json)) == 128


def test_format():
    assert file1_json[len(file1_json)-5:len(file1_json)] == '.json'
    assert file2_json[len(file2_json)-5:len(file2_json)] == '.json'

