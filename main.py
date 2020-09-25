from tkinter import *
from tkinter.ttk import *
import os
window = Tk()
App_Name = "WebODM"
window.geometry("256x256")
window.title(App_Name)


def start():
    os.system("./webodm.sh start")


Start_App = Button(window, text="Simple",command=start)

Start_App.pack()
window.mainloop()
