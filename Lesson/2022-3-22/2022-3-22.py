import pyperclip
import keyboard
import winsound
# spam = "That is alics's cat."
# spam = 'say hi to mother'
# spam = r"\' "
#
# print('''
# 동해물과
#     백두산이 마르고 닳도록
#     하느님이 보우하사 우리나라 만세
#     무궁화 삼천리 화려강산
#     대한사람 대한으로 길이 보전하세
#     ''')
#
# ', '.join(['mango','banana','apple'])
#
# spam = 'my name is hanbit'.split()
#
# 'hello, world'.partition('w')
#
# 'hello'.rjust(10)
# 'hello'.ljust(10)
# 'hello'.ljust(20,'*')
# 'hello'.center(20,'=')

# def play_start_sound():
#     winsound.Beep(440,200)
#     winsound.Beep(440,200)
#
# def play_end_sound():
#     winsound.Beep(440,200)
#     winsound.Beep(440,200)
#     winsound.Beep(440,200)
#
# def report():
#     winsound.Beep(400,500)
#     keyboard.write('shift+windows+w is pressed')
#
# keyboard.add_hotkey('shift+windows+w',report)
# play_start_sound()
# keyboard.wait('esc')
# play_end_sound()
# keyboard.remove_all_hotkeys()
# def process_words(words):
#     word = words.split()
#     dictionary={}
#     print('WORD COUNT'.center(20, '='))
#     for w in word:
#         if w.isalpha():
#             dictionary.setdefault(w,0)
#             dictionary[w]=dictionary[w]+1
#     for w in dictionary:
#         print(w,dictionary[w])
# def Get_Words():
#     words = pyperclip.paste()
#     process_words(words)
#
# keyboard.add_hotkey('shift+windows+w',Get_Words)
# keyboard.wait('esc')
# keyboard.remove_all_hotkeys()

text =  """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[34]"""

word_list = text.split()
word_list=[w for w in word_list if w.isalpha()]
count={}
for w in word_list:
    count.setdefault(w,0)
    count[w]+=1
print("Word Count".center(30,'='))
for key,value in count.items():
    print(key.ljust(20),f'{value:9}')