import os
import random
import datetime
import shutil
import string
import zipfile
#2018182033 이한빛
# os.chdir('C:\ScriptProj')
#file_list=['.doc','.ppt','.pdf','.hwp','.jpg']
# _Length = 5
# string_pool = string.ascii_lowercase
# def make_random_folder():
#     os.mkdir('root_folder')
#     os.chdir('root_folder')
#     for dir in range(0,(random.randint(4,10))):
#         dir_name = ""
#         for i in range(_Length):
#             dir_name+=random.choice(string_pool)
#         os.mkdir(f'{dir_name}')
#     for dir in os.listdir():
#         os.chdir(dir)
#         for file in range(0,(random.randint(1,5))):
#             file_name=""
#             for i in range(_Length):
#                 file_name += random.choice(string_pool)
#             file_name+=file_list[random.randint(0,4)]
#             f= open(file_name,'w')
#             f.close()
#         os.chdir('..')
#
#
# def zip_JPG():
#     for root, subfolders, filename in os.walk('.'):
#         zf = zipfile.ZipFile('final.zip', 'a')
#         for file in filename:
#             if file.endswith('.jpg'):
#                 ctime = os.path.getctime(f'{root}/{file}')
#                 time_format=datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d")
#                 shutil.copy(f'{root}/{file}',f'{root}/{file[:-4]}_{time_format}.jpg')
#                 zf.write(f'{root}/{file[:-4]}_{time_format}.jpg',compress_type=zipfile.ZIP_DEFLATED)
#         zf.close()
# make_random_folder()
# zip_JPG()

ext = ['doc','ppt','pdf','hwp','jpg']
folder_no = 0
def make_random_folders(count):
    global folder_no
    if not count: return
    os.mkdir(f'folder{folder_no}')
    #하나 만들어짐
    os.chdir(f'folder{folder_no}')
    count -= 1
    folder_no+=1

    #랜덤 파일로 채운다
    random_files = [f'file_{folder_no}_{i}.{random.choice(ext)}' for i in range(10)]
    for fn in random_files:
        f = open(fn, 'w')
        f.write('Auto Generated file')
        f.close()

    #남은 갯수만큼, 아래의 촐더를 랜덤하게 만든다.
    while count:
        subcount = random.randint(0,count)
        make_random_folders(subcount)
        count-=subcount
    os.chdir('..')

def zip_jpg_files():
    photo_zip = zipfile.ZipFile('photo.zip','w')
    for root,subfolders,files in os.walk('./folder0'):
        for fn in files:
            if fn.endswith('.jpg'):
                abs_path = root + '/' + fn
                ctime = os.path.getctime(abs_path) # 생성 시간 획득
                cdate = datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d')#년월일 로 변환ㄴ
                fn = fn.replace('.jpg',f'{cdate}.jpg')
                photo_zip.write(abs_path,fn,compress_type=zipfile.ZIP_DEFLATED)
    photo_zip.close()

make_random_folders(100)
zip_jpg_files()