from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image
window = Tk()
def openImg():
    file_name = filedialog.askopenfilename(title='select a img file',
                                           filetype=(("img files (.jpg)", "*.jpg"), ("all files", "*.*")))
    print(file_name)
    tk_image = ImageTk.PhotoImage(file_name)
    # 라벨안에 이미지를 삽입
    Label(window, image=tk_image).pack()
def saveImg():
    file_name = filedialog.asksaveasfilename(title='save file as...',
                                             filetype=(("text file (.jpg)", "*.jpg"), ('all files', "*.*")))
    f = open(f"{file_name}", 'w')

menu = Menu()
menu_file = Menu(menu,tearoff = False)
menu_file.add_command(label = 'Open',command = openImg,accelerator = 'Ctrl+o')
menu_file.add_command(label='Save File',command = saveImg,accelerator = 'Ctrl+s')
menu_file.add_separator()
menu.add_cascade(label='File',menu = menu_file)
window.config(menu= menu)
window.mainloop()