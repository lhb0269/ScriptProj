import re

while(1):
    number = input()

    local_number=['010','02','051','053','032','062','042','052','044','031','033','043','041','063','061','054','055','064']
    phone_re = re.compile(r'\(?(\d{2,3})?\)? *-? *(\d{3,4}) *-? *(\d{4})')

    mo = phone_re.search(number)
    if mo is None:
        print("Wrong number")
    else:
        if mo.group(1) is None:
            print(phone_re.sub(r'(010) \2-\3',number))
        else:
            if mo.group(1) not in local_number:
                print("wrong local number")
            else:
                print('('+mo.group(1)+')'+mo.group(2)+'-'+mo.group(3))