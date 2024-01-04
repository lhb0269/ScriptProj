import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.geometry("960x800")
img_list=[]
def openImg():
    file_name = filedialog.askopenfilename(parent=window,title='select a img file',
                                           filetype=(("image files (.jpg)", "*.jpg"), ("all files", "*.*")))
    img_list.append(file_name)
    draw()
def saveImg():
    file_name = filedialog.asksaveasfilename(title='save file as...',
                                             filetype=(("image file (.jpg)", "*.jpg"), ('all files', "*.*")))
    im.save(f'{file_name}.png')
def draw():
    num = 0
    if img_list is not None:
        for i in img_list:
            img = Image.open(i)
            if num == 0:
                face = img.crop((0, 0, 400, 400))
                im.paste(face,(0,0))
            elif num == 1:
                face = img.crop((400, 0, 800, 400))
                im.paste(face,(400,0))
            elif num == 2:
                face = img.crop((400, 400, 800, 800))
                im.paste(face,(0,400))
            elif num == 3:
                face = img.crop((0, 0, 400, 400))
                im.paste(face,(400,400))
                num=-1
            global tk_image
            tk_image = ImageTk.PhotoImage(im)
            # 라벨안에 이미지를 삽입
            mLabel = Label(window, image=tk_image)
            mLabel.pack()
            num += 1
WIDTH,HEIGHT=800,800
im = Image.new('RGBA',(WIDTH,HEIGHT),'WHITE')

menu = Menu()
menu_file = Menu(menu,tearoff = False)
menu_file.add_command(label = 'Open',command = openImg,accelerator = 'Ctrl+o')
menu_file.add_command(label='Save File',command = saveImg,accelerator = 'Ctrl+s')
menu.add_cascade(label='File',menu = menu_file)
window.config(menu= menu)
window.mainloop()