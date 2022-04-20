from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import re

def stop(event = None):
    window.quit()

window = Tk()
window.title("My first tkinter App")
window.geometry("+0+0")
#window.resizable(False,False)

first_line_frame = Frame()
first_line_frame.pack()

label = Label(first_line_frame,text='Hello tkinter')
label.pack(side=LEFT)

def button_command():
    label.configure(text='pushed')
def change():
    text = label.cget('text')
    text = text[1:] + text[0]
    label.configure(text= text)
    text.tag_configure(text = entry.get())

def change_label_text(event=None):
    new_next = entry.get()
    label.configure(text = new_next)

button = Button(first_line_frame,text = 'change',command  = change,takefocus = False)
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




check_and_radio_frame = LabelFrame(text = 'check and radio')
check_and_radio_frame.pack(side=RIGHT)
text.tag_configure('found',background = 'blue',foreground = 'purple')
ignore_case = IntVar()
checkbutton = Checkbutton(check_and_radio_frame,text = 'Ignore case',variable = ignore_case)
checkbutton.pack(side=RIGHT)
found_color = StringVar(value='blue')
# found_color.set('yellow')
Radiobutton(check_and_radio_frame,text="purple", value="purple", variable=found_color).pack()
Radiobutton(check_and_radio_frame,text="blue", value="blue", variable=found_color).pack()

from tkinter import filedialog
def open_file():
    file_name = filedialog.askopenfilename(title = 'select a text file',filetype=(("text files (.txt)","*.txt"),("all files","*.*")))
    text.delete("1.0",END)
    f = open(f"{file_name}","r")
    while True:
        line = f.readline()
        if not line:
            break
        text.insert(END,f"{line}")
def save_file():
    file_name = filedialog.asksaveasfilename(title = 'save file as...',filetype = (("text file (.txt)","*.txt"),('all files',"*.*")))
    f= open(f"{file_name}",'w')
    print(text.get("1.0",END),file = f)
def select_pattern(event=None):
    print(history_listbox.curselection())

    pattern =""
    for i in history_listbox.curselection():
        pattern=history_listbox.get(i)
    target = re.compile(pattern)
    input_text = text.get("1.0",END)
    lines = input_text.splitlines()

    text.tag_remove('found',"1.0",END)
    for i,line in enumerate(lines):
        for mo in target.finditer(line):
            #print(mo)
            text.tag_add('found', f"{i + 1}.0+{mo.span()[0]}chars", f"{i + 1}.0+{mo.span()[1]}chars")



history_listbox = Listbox(selectmode = 'single',height = 5)
history_listbox.insert(END,'Python')
history_listbox.insert(END,'[a-zA-Z]+')
history_listbox.pack()

history_listbox.bind('<<ListboxSelect>>',select_pattern)


menu = Menu()
menu_file = Menu(menu,tearoff = False)
menu_file.add_command(label = 'Open',command = open_file,accelerator = 'Ctrl+o')
menu_file.add_command(label='Save File',command = save_file,accelerator = 'Ctrl+s')
menu_file.add_separator()
menu_file.add_command(label = 'Quit',accelerator = 'Ctrl+q')

menu.add_cascade(label='File',menu = menu_file)

window.config(menu= menu)
window.bind("<Escape>",stop)
window.bind("<Control-x>",stop)
window.mainloop()