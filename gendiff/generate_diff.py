#!/usr/bin/env python3
from parser_diff import parser_diff
from make_str_diff import make_str_diff
from make_dict_diff import make_dict_diff

# file1 = 'tests/fixtures/file1.json'
# file2 = 'tests/fixtures/file2.json'


def generate_diff(file1, file2):

    result_list = []

    file_path1 = parser_diff(file1)
    file_path2 = parser_diff(file2)

    result_list = make_dict_diff(file_path1, file_path2)

    return make_str_diff(result_list)

    # return result_dict
    # return json.dumps(result_dict, indent=4, sort_keys=False)

# print(generate_diff(file1, file2))
