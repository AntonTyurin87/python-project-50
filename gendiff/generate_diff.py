#!/usr/bin/env python3
from gendiff.parser_diff import parser_diff
from gendiff.make_dict_diff import make_dict_diff

# file1 = 'tests/fixtures/file1.json'
# file2 = 'tests/fixtures/file2.json'


def generate_diff(file1, file2):

    result_list = []

    file_path1 = parser_diff(file1)
    file_path2 = parser_diff(file2)

    for i in file_path1:
        if i in file_path2 and file_path1.get(i) == file_path2.get(i):
            result_list.append((i, ' ', file_path1.get(i)))
            file_path2.pop(i)
        elif i not in file_path2:
            result_list.append((i, '-', file_path1.get(i)))
        elif i in file_path2 and file_path1.get(i) != file_path2.get(i):
            result_list.append((i, '-', file_path1.get(i)))
            result_list.append((i, '+', file_path2.get(i)))
            file_path2.pop(i)

    if len(file_path2) != 0:
        for j in file_path2:
            result_list.append((j, '+', file_path2.get(j)))

    return make_dict_diff(result_list)

    # return result_dict
    # return json.dumps(result_dict, indent=4, sort_keys=False)

# print(generate_diff(file1, file2))
