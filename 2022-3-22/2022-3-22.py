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
def process_words(words):
    word = words.split()
    dictionary={}
    print('WORD COUNT'.center(20, '='))
    for w in word:
        if w.isalpha():
            dictionary.setdefault(w,1)
            dictionary[w]=dictionary[w]+1
    for w in dictionary:
        print(w,dictionary[w])
def Get_Words():
    words = pyperclip.paste()
    process_words(words)


keyboard.add_hotkey('shift+windows+w',Get_Words)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()