from tkinter import *
from back import Database
database=Database("books.db")

window=Tk()
window.wm_title("Book Store")

def get_select(event):
	try:
		global selected_tuple
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		title.delete(0,END)
		title.insert(END,selected_tuple[1])
		author.delete(0,END)
		author.insert(END,selected_tuple[2])
		year.delete(0,END)
		year.insert(END,selected_tuple[3])
		isbn.delete(0,END)
		isbn.insert(END,selected_tuple[4])
	except IndexError:
		pass
def view_read():
	list1.delete(0,END)
	for row in database.view():
		list1.insert(END,row)
def view_search():
	list1.delete(0,END)
	for row in database.search(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
		list1.insert(END,row)
def view_add():
		database.insert(title_var.get(),author_var.get(),year_var.get(),isbn_var.get())
		list1.delete(0,END)
		for row in database.view():
			list1.insert(END,row)
		
def view_update():
	list1.delete(0,END)
	for row in database.update(selected_tuple[0],title_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
		list1.insert(END,row)
def view_delete():
	list1.delete(0,END)
	for row in database.delete(selected_tuple[0]):
		list1.insert(END,row)

		
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_var=StringVar()
title=Entry(window,textvariable=title_var)
title.grid(row=0,column=1,columnspan=2)

l2=Label(window,text="Author")
l2.grid(row=0,column=3)
author_var=StringVar()
author=Entry(window,textvariable=author_var)
author.grid(row=0,column=4,columnspan=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)
year_var=StringVar()
year=Entry(window,textvariable=year_var)
year.grid(row=1,column=1,columnspan=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=3)
isbn_var=StringVar()
isbn=Entry(window,textvariable=isbn_var)
isbn.grid(row=1,column=4,columnspan=2)

list1=Listbox(window,height=15,width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=9)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
	
list1.bind('<<ListboxSelect>>',get_select)
	
b1=Button(window,text="VIEW ALL",width=12,command=view_read)
b1.grid(row=2,column=4,rowspan=2)
b2=Button(window,text="Search",width=12,command=view_search)
b2.grid(row=3,column=4,rowspan=2)
b3=Button(window,text="Add",width=12,command=view_add)
b3.grid(row=4,column=4,rowspan=2)
b4=Button(window,text="Update",width=12,command=view_update)
b4.grid(row=5,column=4,rowspan=2)
b5=Button(window,text="Delete",width=12,command=view_delete)
b5.grid(row=6,column=4,rowspan=2)
b6=Button(window,text="Exit",width=12,command=window.destroy)
b6.grid(row=7,column=4,rowspan=2)


window.mainloop()