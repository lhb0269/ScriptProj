import os

os.chdir('c:/Python')

file_dict={}
total_size = 0

for root,subfolders,filename in os.walk('.'):
     (f'{root}')
     (f'{subfolders}')
     (f'{filename}')
     #total_size = os.path.getsize(f'{filename}')
     file_dict[os.path.abspath(f'{filename}')]=total_size

for k,v in file_dict.items():
    print(k,v)
    print('\n')
# for fn in os.listdir():
#     total_size = os.path.getsize(fn)
#     print(fn,total_size)


#result = sorted(data.items(),key=lambda x:x[1],reverse= True)

#print(total_size)