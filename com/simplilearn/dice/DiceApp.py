from tkinter import *
from tkinter import ttk
import random

# Craete the UI Object
tk=Tk()


tk.geometry("400x400")
style=ttk.Style(tk)
style.theme_use('clam')
tk.title("Simplilearn Dice")

label=Label(tk,text="",font=("times",260))

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button=Button(tk,text="Let's Roll ...",width=41,height=6,font=11,bg="white",bd=3,command=roll)
button.pack(padx=10,pady=10)


tk.mainloop()
