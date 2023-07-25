from gendiff.make_str_diff import make_str_diff
from tests.fixtures.right_answer import right_answer

result_list = [('host', ' ', 'hexlet.io'), ('timeout', '-', 50), ('timeout', '+', 20), ('proxy', '-', '123.234.53.22'), ('follow', '-', False), ('verbose', '+', True)]

def tast_make_str_diff():
    assert  make_str_diff(result_list) == right_answer
