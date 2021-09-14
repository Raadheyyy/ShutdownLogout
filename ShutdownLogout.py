from tkinter import *

import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

master = Tk()
master.geometry("200x200")
master.title("ShutdownLogout")
master.configure(bg = "light blue")

Button(master, text="Shutdown", command = shutdown).place(x = 67, y= 20)
Button(master, text="Restart", command = restart).place(x = 75, y= 70)
Button(master, text="Log out", command = logout).place(x = 72, y= 120)

mainloop()