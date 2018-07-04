#ASSIGNMENT-18(GUI 2)
#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *


def show():
      k = l.get(ACTIVE)
      v = contact[k]
      label_1.config(text=k)
      label_2.config(text=v)
contact={ "A AARON SAMUEL":'546565656767',"A AARON SAMUEL":'656565577676',"BHUVAN RAJ":'65656565656',"C S Rithica":'5656565656',"DIKSHI JAIN":'6897323233',"K V A SHREE VYBHAV":'9675645654767',"KATHEEB MUZAMMIL":'65654765876754',"Kavin Mukilan":'4543657657' ,"MATHEW JACOB THARAKAN":'989978665645',"P CAROLYN NIRMALA":'6565465466545',"R A MADAV MAHESH":'9786656688',"R Pranav":'798985676879',"S SNEGHA ANTONY RAJ":'990898978989',"S SNEHASHREE":'89898797989',"V Mithik":'98989898989',"Vezhavendhan":'8989798989',"Vineet Sarda":'98989898798' }
root=Tk()

root.resizable(False,False)
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,width=50, height=10,yscrollcommand=s.set)
for k in contact.keys():
      l.insert(END,k)
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
f1=Frame(root)
f1.pack(side=TOP)
label_1=Label(f1,width=30,text="Name",bg="powder blue")
label_1.pack()
label_2=Label(f1,width=30,text="Contact",bg="powder blue")
label_2.pack()
but=Button(f1,text="Select",width=30,command=show)
but.pack()
root.mainloop()


#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.


def insert():
      k = entry.get()
      v = entry_1.get()
      contact[k] = v
      l.insert(END,k)
      print(contact)



contact = {"A AARON SAMUEL": '546565656767', "A AARON SAMUEL": '656565577676', "BHUVAN RAJ": '65656565656',
           "C S Rithica": '5656565656', "DIKSHI JAIN": '6897323233', "K V A SHREE VYBHAV": '9675645654767',
           "KATHEEB MUZAMMIL": '65654765876754', "Kavin Mukilan": '4543657657', "MATHEW JACOB THARAKAN": '989978665645',
           "P CAROLYN NIRMALA": '6565465466545', "R A MADAV MAHESH": '9786656688', "R Pranav": '798985676879',
           "S SNEGHA ANTONY RAJ": '990898978989', "S SNEHASHREE": '89898797989', "V Mithik": '98989898989',
           "Vezhavendhan": '8989798989', "Vineet Sarda": '98989898798'}
root = Tk()

root.resizable(False, False)
s = Scrollbar(root)
s.pack(side=RIGHT, fill=Y)
l = Listbox(root, width=50, height=10, yscrollcommand=s.set)
for k in contact.keys():
      l.insert(END, k )
l.pack(side=LEFT, fill=BOTH)
s.config(command=l.yview())
f1 = Frame(root)
f1.pack(side=TOP)
label_1 = Label(f1, width=30, text="Name", bg="powder blue")
label_1.pack()
entry=Entry(f1)
entry.pack()
entry_1=Entry(f1)
entry_1.pack()
label_2 = Label(f1, width=30, text="Contact", bg="powder blue")
label_2.pack()
but = Button(f1, text="Enter", width=30, command=insert)
but.pack()
root.mainloop()