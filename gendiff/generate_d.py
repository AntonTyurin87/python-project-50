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
        if i in file_path2 and file_path1.get(i) == file_path2.get(i) and len(file_path2) != 0:
            result_list.append((i,' ',file_path1.get(i)))
            file_path2.pop(i)
        elif i not in file_path2:
            result_list.append((i,'-',file_path1.get(i)))
        elif i in file_path2 and file_path1.get(i) != file_path2.get(i) and len(file_path2) != 0:
            result_list.append((i,'-',file_path1.get(i)))
            result_list.append((i,'+',file_path2.get(i)))
            file_path2.pop(i)

    if len(file_path2) != 0:
        for j in file_path2:
            result_list.append((j,'+',file_path2.get(j)))

    for k in sorted(result_list, key=lambda point: (point[0])):
        result_dict.update({k[1] + ' ' + k[0]: k[2]})

        #print(result_dict)

    return json.dumps(result_dict, indent=4, sort_keys=False)  # json.dumps(dic, indent=4, sort_keys=True)) result_dict

'''
    result_list = list(result_dict)
    result_list.sort()

    for k in result_list:
        #print(k[len(k)-1:len(k)])
        if k[len(k)-1:len(k)] == '+' or k[len(k)-1:len(k)] == '-':
            key_string = k[len(k)-1:len(k)] + ' ' + k[0:len(k)-1]
            #print(key_string)
        else:
            key_string = k

        dict.update({key_string: result_dict.get(k)})

    return dict
'''
 

#print(generate_diff(file1, file2))
        
'''

#file_path1 = json.load(open(file1))
#file_path2 = json.load(open(file2))



#a = json.load(open('fixtures/file1.json'))

for i in file_path1:

    print(i)
    print(i in file_path2)
    print('---------------')
#print(sorted(a.items()))

json.load(open('path/to/file.json'))


def generate_diff(file1, file2):
    result_dict = {}
    result_list = []

    dict = {}

    file_path1 = json.load(open(file1))
    file_path2 = json.load(open(file2))

    #file_path1 = sorted(json.load(open(file1).items()))
    #file_path2 = sorted(json.load(open(file2).items()))

    for i in file_path1:
        #print(i)
        if i in file_path2 and file_path1.get(i) == file_path2.get(i) and len(file_path2) != 0:
            result_dict.update({i:file_path1.get(i)})
            file_path2.pop(i)
        elif i not in file_path2:
            result_dict.update({str(i + '-'):file_path1.get(i)})
        elif i in file_path2 and file_path1.get(i) != file_path2.get(i) and len(file_path2) != 0:
            result_dict.update({str(i + '-'):file_path1.get(i)})
            result_dict.update({str(i + '+'):file_path2.get(i)})
            file_path2.pop(i)

    if len(file_path2) != 0:
        for j in file_path2:
            result_dict.update({str(j + '+'):file_path2.get(j)})


    result_list = list(result_dict)
    result_list.sort()

    for k in result_list:
        #print(k[len(k)-1:len(k)])
        if k[len(k)-1:len(k)] == '+' or k[len(k)-1:len(k)] == '-':
            key_string = k[len(k)-1:len(k)] + ' ' + k[0:len(k)-1]
            #print(key_string)
        else:
            key_string = k

        dict.update({key_string: result_dict.get(k)})

    return dict


'''