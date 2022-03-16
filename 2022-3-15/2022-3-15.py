import math
# population = 51_628_117
# message = '아기 많이 낳읍시다.'
#
# print('인구는',population,'명입니다.','원주율은',math.pi,'입니다.',message)
# print('인구는 %d 명입니다. 원주율은 %.6f 입니다. %s'%(population,math.pi,message))
#
# print(f"인구는 {population} 명입니다. 원주율은{math.pi} 입니다.{message}")
# print(f"인구는 {population:,} 명입니다. 원주율은 {math.pi:.6f} 입니다. {message}")
#
# print(f"브레이스는 {{}} 이렇게 씁니다.")

# f= lambda x,y:x+y
# print(f(10,20))
#
# f= lambda x,y,z : x+y+z
# print(f(1,2,3))
#
data = range(0,100)
#
# f= lambda x:x**2
# map(f,data)
#
# print(list(map(f,data)))
#
# print(list(map(f,map(f,data))))


# f= lambda x:x%2==0
# print(list(filter(f,data)))

def merge(*str):
    result =''
    num = 0
    num2 = 0
    for s in str:
        num+=1
    for s in str:
        num2+=1
        if num2 >= num:
            result+='and '+s
        else:
            result += s +','
    return result

def merge2(*fruits):
    result =''
    for fruit in fruits[:-1]:
        result += fruit + ', '
    result += 'and ' + fruits[-1] if len(fruits) > 1 else fruits[-1]
    return result


final = merge2('orange','apple','mango','banana','peanut')
print(final)
print(type(final))