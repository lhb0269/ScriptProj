import os
file_info = {}

#폴더 서치해서 파일을 찾아줘야 할것...

for root,subfolders,files in os.walk('c:/Python'):
    for fn in files:
        abs_path = root + '/' + fn
        size = os.path.getsize(abs_path)
        file_info[abs_path] = size


def get_key(x):
    return x[1]
file_info_list = [item for item in file_info.items()]
sorted_file_info_lst = sorted(file_info_list,key = get_key,reverse= True)
