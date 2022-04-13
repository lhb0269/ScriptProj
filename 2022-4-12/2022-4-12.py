import traceback

raise ValueError
raise ValueError('Too Young')
raise Exception
raise Exception('this is Error')


try:
    age = int(input('enter age'))
    if age < 18:
        raise ValueError('Too Young')
# except ValueError as err:
#     print(err)
except Exception as err:
    print(f'{err=},{type(err)=}')

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym,w,h in (('*',4,4),('0',20,5),('x',1,3),('ZZ',3,3)):
    boxPrint(sym,w,h)

def bacon():
    try:
        raise Exception('Error')
    except:
        ef = open('error_stack.txt','w')
        for line in traceback.format_stack():
            ef.write(line)
        ef.close()

def spam():
    bacon()

spam()


data = 100

assert data == 100

assert  data < 100