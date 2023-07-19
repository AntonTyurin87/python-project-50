#!/usr/bin/env python3
import json

file1 = 'fixtures/file1.json'
file2 = 'fixtures/file2.json'


def generate_diff(file1, file2):
    result_dict = {}
    result_list = []

    file_path1 = json.load(open(file1))
    file_path2 = json.load(open(file2))

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

    for k in sorted(result_list, key=lambda point: (point[0])):
        result_dict.update({k[1] + ' ' + k[0]: k[2]})

    # return result_dict
    return json.dumps(result_dict, indent=4, sort_keys=False)
