#!/usr/bin/env python3
from gendiff.make_dict_diff import make_dict_diff

file_path1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
file_path2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_make_dict_diff():
    assert make_dict_diff(file_path1, file_path2) == [('host', ' ', 'hexlet.io'), ('timeout', '-', 50), ('timeout', '+', 20), ('proxy', '-', '123.234.53.22'), ('follow', '-', False), ('verbose', '+', True)]