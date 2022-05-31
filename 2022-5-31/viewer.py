from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

def show_image(img):
    window = Tk()   # window
    #img " PIL image --> tkinter image 위젯으로 변환
    tk_image = ImageTk.PhotoImage(img)
    
    #라벨안에 이미지를 삽입
    Label(window,image = tk_image).pack()

    def stop(event = None):
        window.destroy()

    window.bind('<Escape>',stop)
    window.bind('q',stop)
    window.mainloop()


def show_images(img1,img2):
    window = Tk()  # window
    # img " PIL image --> tkinter image 위젯으로 변환
    tk_image1 = ImageTk.PhotoImage(img1)
    tk_image2 = ImageTk.PhotoImage(img2)

    # 라벨안에 이미지를 삽입
    Label(window, image=tk_image1).pack()
    Label(window, image=tk_image2).pack()

    def stop(event=None):
        window.destroy()

    window.bind('<Escape>', stop)
    window.bind('q', stop)
    window.mainloop()

