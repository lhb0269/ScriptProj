from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import re

def stop(event = None):
    window.quit()

window = Tk()
window.title("My first tkinter App")
#window.geometry("640x480+100+100")
#window.resizable(False,False)

first_line_frame = Frame()
first_line_frame.pack()

label = Label(first_line_frame,text='Hello tkinter')
label.pack(side=LEFT)

def button_command():
    label.configure(text='pushed')
def rotate():
    text = label.cget('text')
    text = text[1:] + text[0]
    label.configure(text= text)
def change_label_text(event=None):
    new_next = entry.get()
    label.configure(text = new_next)


button = Button(first_line_frame,text = 'Push',command  = rotate,takefocus = False)
button.pack(side = RIGHT)

entry = Entry(width = 100)
entry.bind('<Return>',change_label_text)
entry.pack()

wiki_python ="""
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.

Python consistently ranks as one of the most popular programming languages.
"""
text = ScrolledText(width = 50,height = 10,font=('Aria',10))
text.insert(END,wiki_python)
text.pack()

text.tag_configure('found',background = 'yellow',foreground = 'red')
ignore_case = IntVar()
checkbutton = Checkbutton(text = 'Ignore case',variable = ignore_case)
checkbutton.pack()

def select_pattern(event=None):
    print(history_listbox.curselection())

    pattern =""
    for i in history_listbox.curselection():
        pattern=history_listbox.get(i)
    target = re.compile(pattern)
    input_teext = text.get("1.0",END)
    lines = input_teext.splitlines()

    text.tag_remove('found',"1.0",END)
    for i,line in enumerate(lines):
        for mo in target.finditer(line):
            print(mo)
            text.tag_add('found',f"{i+1}.0+{mo.span()[0]}chars",f"{i+1}.0+{mo.span()[1]}chars")

history_listbox = Listbox(selectmode = 'single',height = 5)
history_listbox.insert(END,'Python')
history_listbox.insert(END,'[a-zA-Z]+')
history_listbox.pack()

history_listbox.bind('<<ListboxSelect>>',select_pattern)


window.bind("<Escape>",stop)
window.bind("<Control-x>",stop)
window.mainloop()