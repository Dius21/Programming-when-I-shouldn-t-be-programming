from tkinter import *
from tkinter.ttk import *

def main():
    root = Tk()

    root.title("uga buga")

    label = Label(root,text="UGA BUGA BUGA!!").pack()
    frame = Frame(root)

    frame.pack()

    button = Button(frame, text='Greek')
    button.pack()

    root.mainloop()