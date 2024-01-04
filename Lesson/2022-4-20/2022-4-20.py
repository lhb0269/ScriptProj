from tkinter import *
from tkinter.ttk import *

window=Tk()
window.geometry("+0+0")
window.resizable(False,False)
def stop(Event=None):
    window.quit()
window.bind('<Escape>',stop)

combo_frame = LabelFrame(text='Pattern')
combo_frame.pack(fill=BOTH,padx = 5,pady = 5)

def enter_new_pattern(event = None):
    new_pattern = combobox.get()
    main_text.insert("1.0",f"new pattern {new_pattern}is entered")
    print (combobox['values'])
    combobox['values']+=(new_pattern,)

combobox = Combobox(combo_frame,values=['Python','[a-zA-Z]+'])
combobox.bind('<Return>',enter_new_pattern)
combobox.pack(fill=BOTH)

text_frame=LabelFrame(text = 'Log')
text_frame.pack(padx =5,pady= 5)

from tkinter.scrolledtext import ScrolledText
source_text ="""
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.

Python consistently ranks as one of the most popular programming languages.
"""

main_text = ScrolledText(text_frame)
#main_text.insert(END,source_text)
main_text.pack()



command_frame = LabelFrame(text = 'command')
command_frame.pack(fill=BOTH,padx =5,pady= 5)
from tkinter import filedialog
def open_file():
    file_name = filedialog.askopenfilename(title = 'select a text file',filetype=(("text filies (.txt)","*.txt"),("all files","*.*")))
    main_text.insert("1.0",f"file {file_name} is selected.\n")

def commad_a():
    main_text.delete("1.0",END)
    pass
def commad_b():
    #main_text.insert(END,source_text)
    main_text.insert("1.0",f"current pattern is {combobox.get()}")
    pass

def commad_c():
    #main_text.replace("1.0","1.6",'PYTHON PYTHON')
    open_file()
    pass

def commad_d():
    pass


Button(command_frame,command = commad_a,text='Command A').pack(side=LEFT,expand = True,fill=BOTH,padx = 5)
Button(command_frame,command = commad_b,text='Command B').pack(side=LEFT,expand = True,fill=BOTH,padx = 5)
Button(command_frame,command = commad_c,text='Command C').pack(side=LEFT,expand = True,fill=BOTH,padx = 5)
Button(command_frame,command = commad_d,text='Command D').pack(side=LEFT,expand = True,fill=BOTH,padx = 5)


menu = Menu()
menu_file = Menu(menu,tearoff = False)
menu_file.add_command(label = 'Open',command = open_file(),accelerator = 'Ctrl+o')
menu_file.add_command(label='Save File',accelerator = 'Ctrl+s',state = 'disable')
menu_file.add_separator()
menu_file.add_command(label = 'Quit',accelerator = 'Ctrl+q')

menu.add_cascade(label='File',menu = menu_file)


menu_edit = Menu(menu,tearoff = False)
menu_edit.add_command(label = 'Open',accelerator = 'Ctrl+o')
menu_edit.add_command(label='Save File',accelerator = 'Ctrl+s',state = 'disable')
menu_edit.add_separator()
menu_edit.add_command(label = 'Quit',accelerator = 'Ctrl+q')

menu.add_cascade(label='Edit',menu = menu_edit)

window.config(menu=menu)
window.mainloop()