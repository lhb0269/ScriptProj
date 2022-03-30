import re
import exrex
pre = re.compile(r'''
02|051|053|010''',re.VERBOSE)

pre = re.compile(r'''
\((02|051|053|010)\)''',re.VERBOSE)


pre = re.compile(r'''
    ^
    (
    (02|051|053|010)
    |
    (\(
        [ ]*
        (02|051|053|010)
        [ ]*
    \))
   [ ]*
   -?
   [ ]*
   )?
   [ ]*
   \d{3,4}
   [ ]*
   -?
   [ ]*
   \d{4}
   $
   ''',re.VERBOSE)


pattern = (r'''
     ^
    (
    (02|051|053|010)
    |
    (\(
        [ ]*
        (02|051|053|010)
        [ ]*
    \))
   [ ]*
   -?
   [ ]*
   )?
   [ ]*
   \d{3,4}
   [ ]*
   -?
   [ ]*
   \d{4}
   $
   ''')

final_pattern = re.sub(r'[ ]{2,}|\t|\n', '',pattern)
good_list=[]
for i in range(1000):
    print(exrex.getone(final_pattern,2))
    good_list.append(exrex.getone(final_pattern,2))

for s in good_list:
    print(s)

good_str=['(02-8041-1234)','02-1234-1234','010','( 02 )','(  010   )','010-1234-12345']
bad_str=['(02','01','999','(0 2)','( 05 1)']

def test_good():
    for s in good_str:
        mo = pre.search(s)
        if not mo:
            print('Bad')
            print(s)

def test_bad():
    for s in bad_str:
        mo = pre.search(s)
        if mo:
            print('Bad')
            print(s)

def test_all():
    test_good()
    test_bad()

test_all()

password_re = re.compile(r'[a-zA-z]{10,}') #영문자 10자 이상
password_re = re.compile(r'[0123456789a-zA-z]{10,}') #영어와 숫자 10자 이상



local_number=['010','02','051','053','032','062','042','052','044','031','033','043','041','063','061','054','055','064']
phone_re = re.compile(r'\(?(\d{2,3})?\)? *-? *(\d{3,4}) *-? *(\d{4})')

for s in good_list:
    mo = phone_re.search(s)
    if mo is None:
        print(s,"Wrong number")
    else:
        if mo.group(1) is None:
            pass
            print(phone_re.sub(r'(010) \2-\3',s))
        else:
            if mo.group(1) not in local_number:
                print(s,"wrong local number")
            else:
                pass
                print('('+mo.group(1)+')'+mo.group(2)+'-'+mo.group(3))


