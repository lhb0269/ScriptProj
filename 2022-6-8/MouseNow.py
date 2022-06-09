from tkinter  import *
from tkinter.ttk import *
import pyautogui

window=Tk()
window.title("Mouse Now")
window.geometry("300x100")
window.resizable(FALSE,FALSE)

x,y=pyautogui.position()
loc_text = f"x={x:4},y={y:4}"
label = Label(text= loc_text)
label.pack()

def update_mouse_position():
    global label
    x,y = pyautogui.position()
    loc_text = f"x={x:4} y={y:4}"
    label.configure(text=loc_text)
    window.after(10,update_mouse_position)

window.attributes('-topmost',True)
window.after(10,update_mouse_position)
window.mainloop()