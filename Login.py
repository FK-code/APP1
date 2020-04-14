from tkinter import * 
from tkinter import messagebox


t=Tk()
t.geometry('400x200')
var= int()

f=Frame(t)
f.grid()

l1=Label(t,text="USERNAME::",font="ariel", padx=5, pady=5)
l1.grid(row=0,column=0)
l2=Label(t,text="PASSWORD::",font="ariel", padx=5, pady=5)
l2.grid(row=1,column=0)
e1=Entry(t,font="ariel")
e1.grid(row=0,column=1)
e2=Entry(t,show="*")
e2.grid(row=1,column=1)


def log():
 messagebox.showinfo(t,"login Succesfully")


b1=Button(t,text="Login",command=log,relief="raised")
b1.grid(row=6,column=0)


t.mainloop()

