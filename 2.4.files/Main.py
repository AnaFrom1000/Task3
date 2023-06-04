import os
dict={}

def open_file(file_name):
    current=os.getcwd()
    folder_name = 'sorted'
    full_path=os.path.join(current, folder_name, file_name)
    with open (full_path, encoding='utf-8') as file:
        res=file.readlines()
        dict[file_name]=res

open_file('1.txt')
open_file('2.txt')
open_file('3.txt')

#print(dict)
print(len(dict['1.txt']))
sorted_dict={}
sorted_keys=sorted(dict, key=lambda k: len(dict[k]), reverse=False)
for w in sorted_keys:
    sorted_dict[w] = dict[w]




with open ('New_file.txt', 'a', encoding='utf-8') as file:
    for key in sorted_dict:
        

        result=str(f'{key} \n {len(sorted_dict[key])} \n')
        file.writelines(result)
        file.writelines(sorted_dict[key])
        file.writelines('\n')
        

