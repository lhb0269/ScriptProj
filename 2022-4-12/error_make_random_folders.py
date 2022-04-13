import os
import random
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
folder_no = 0

ext = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']

# quota 를 가지고서, 폴더에 들어간 후에, 남겨진 quota 를 다시 분배해서 들어가면 된다.


def make_random_folders(count):
    global folder_no

    if not count:
        raise Exception('count 값이 없습니다. 꼭 있어야 해용~~')

    logging.info(f'created folder{folder_no}')
    #print(f'created folder{folder_no}')

    os.mkdir(f'folder{folder_no}')
    os.chdir(f'folder{folder_no}')

    folder_no += 1
    count -= 1
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount


report_home = 'c:/ScriptProj/TestFolder'


def make_random_root_folder():
    os.mkdir('root_folder')
    os.chdir('root_folder')
    make_random_folders(0)
    os.chdir('..')
try:
    os.chdir(report_home)
    make_random_root_folder()
except Exception as err:
    print('error : ',err)
#크게 2가지 문제점