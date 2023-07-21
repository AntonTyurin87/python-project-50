#!/usr/bin/env python3
import pytest
from gendiff.generate_diff import generate_diff


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '''{
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True
}'''


def test_type_test_generate_diff():
    text = 'text'
    assert type(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')) == type(text)


def len_text_test_generate_diff():
    assert len(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')) == 128
    