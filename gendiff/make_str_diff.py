#!/usr/bin/env python3

def make_dict_diff(result_list):
    result_dict = {}
    result_str = ''

    for k in sorted(result_list, key=lambda point: (point[0])):
        result_dict.update({k[1] + ' ' + k[0]: k[2]})

    for d in result_dict:
        e = result_dict.get(d)
        result_str += '    ' + str(d) + ':' + ' ' + str(e) + '\n'

    result_str = '{' + '\n' + result_str + '}'

    return result_str
