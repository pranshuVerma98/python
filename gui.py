from tkinter import *

def km_to_mile():
	t1.insert(END,float(e1_var.get())*1.6)
	
window=Tk()

b1=Button(window,text="convert",command=km_to_mile)
e1_var=StringVar()
e1=Entry(window,textvariable=e1_var)
t1=Text(window,height=1,width=20)

e1.grid(row=0,column=0,columnspan=2)
b1.grid(row=4,column=2,rowspan=2)
t1.grid(row=0,column=3)
window.mainloop()