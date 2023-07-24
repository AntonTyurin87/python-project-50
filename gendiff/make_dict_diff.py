#!/usr/bin/env python3


def make_dict_diff(file_path1, file_path2):

    result_list = []

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

    return result_list
