import os
import random
import datetime
import shutil
import string
import zipfile
#2018182033 이한빛
os.chdir('C:\ScriptProj')
file_list=['.doc','.ppt','.pdf','.hwp','.jpg']
_Length = 5
string_pool = string.ascii_lowercase
def make_random_folder():
    os.mkdir('root_folder')
    os.chdir('root_folder')
    for dir in range(0,(random.randint(4,10))):
        dir_name = ""
        for i in range(_Length):
            dir_name+=random.choice(string_pool)
        os.mkdir(f'{dir_name}')
    for dir in os.listdir():
        os.chdir(dir)
        for file in range(0,(random.randint(1,5))):
            file_name=""
            for i in range(_Length):
                file_name += random.choice(string_pool)
            file_name+=file_list[random.randint(0,4)]
            f= open(file_name,'w')
            f.close()
        os.chdir('..')


def zip_JPG():
    for root, subfolders, filename in os.walk('.'):
        zf = zipfile.ZipFile('final.zip', 'a')
        for file in filename:
            if file.endswith('.jpg'):
                ctime = os.path.getctime(f'{root}/{file}')
                time_format=datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d")
                shutil.copy(f'{root}/{file}',f'{root}/{file[:-4]}_{time_format}.jpg')
                zf.write(f'{root}/{file[:-4]}_{time_format}.jpg',compress_type=zipfile.ZIP_DEFLATED)
        zf.close()
make_random_folder()
zip_JPG()
