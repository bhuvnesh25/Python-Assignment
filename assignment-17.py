# ASSIGNMENT-17(GUI)
# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *

display=Tk()
t=Label(display,text="Hello World!")
t.pack(fill=X,side=TOP)
b1=Button(display,text="Close",command=exit)
b1.pack(fill=X,side=BOTTOM)
display.mainloop()



# Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
def show():
    print("Hey! hello friend ")
play=Tk()
frame=Frame(play)
frame.pack(side=TOP)
t=Label(frame,text="Hello! action to perform",width=25)
t.grid(row=0,column=3)
b1=Button(frame,text="CLOSE",command=exit,width=25)
b1.grid(row=3,column=3)
b2=Button(frame,text="NEXT",command=show,width=25)
b2.grid(row=5,column=3)
play.mainloop()
# Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

def display():
    b.config(text="Let's Play!")

play=Tk()
b=Label(play,text="Hello! action to perform",width=25)
b.grid(row=0,column=5)
b1=Button(play,text="CLOSE",command=exit,width=25)
b1.grid(row=3,column=5)
b2=Button(play,text="click!",command=display,width=25)
b2.grid(row=5,column=5)
play.mainloop()

# Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

def function():
    print(en1.get())
    print(en2.get())
take = Tk()
label_1=Label(take,text="First Name:")
label_1.grid(row=0)
label_2=Label(take,text=" Last Name:")
label_2.grid(row=1)
en1=Entry(take)
en1.grid(row=0,column=1)
en2=Entry(take)
en2.grid(row=1,column=1)
b1=Button(take,text="Save",command=function)
b1.grid(row=0,column=2)
b2=Button(take,text="Quit",command=exit)
b2.grid(row=1,column=2)
take.mainloop()