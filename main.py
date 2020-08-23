import pyautogui
from tkinter import Tk, Label

root = Tk()
root.title('MousePos')
root.attributes("-topmost", True)
lab = Label(root)
lab.pack()


def get_mouse_position():
    (x, y) = pyautogui.position()
    lab.config(text=f'{x,y}')
    root.after(1, get_mouse_position)


if __name__ == '__main__':
    get_mouse_position()
    root.mainloop()