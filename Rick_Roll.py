from tkinter import *
import webbrowser
from tkinter import messagebox
import pyautogui
import random
import os
import sys

root = Tk()
root.title("Rickroll.exe")
root.iconbitmap(bitmap=os.path.basename(sys.argv[0]))
root.overrideredirect(1)
root.attributes("-topmost", True)

def Position():
    if 'withdrawn' != root.state():
        root.geometry("+%d+%d" % (pyautogui.position()[0]-100, pyautogui.position()[1]-150))
        root.after(1, Position)

def Rick_roll():
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLahKLy8pQdCM0SiXNn3EfGIXX19QGzUG3")
    root.withdraw()
    root.after(3000)
    messagebox.showwarning(title="Oh no too bad", message="You've been Rick Rolled")
    root.quit()
    Roll_loop()

def Roll_loop():
    if 1 == random.randint(1, 250):
        Rick_roll()
    else:
        root.after(1000)
        Roll_loop()

Button(root, text ="Click Me!!!", command = Rick_roll, height=5, width=10, bg="#E50000", fg="white", font="Helvetica 24 bold").pack()

root.after(100, Position)

root.mainloop()
