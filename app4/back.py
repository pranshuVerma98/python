import sqlite3

class Database:
	def __init__(self,db):
		self.conn=sqlite3.connect(db)
		self.curr=self.conn.cursor()
		self.curr.execute("create table if not exists BOOK(id integer PRIMARY KEY,Title text,Author text,Year int,ISBN int)")
		self.conn.commit()
	
	def view(self):
		self.curr.execute("select * from BOOK")
		rows=self.curr.fetchall()
		return rows

	def insert(self,title,author,year,isbn):
		self.curr.execute("insert into BOOK values(NULL,?,?,?,?)",(title,author,year,isbn))
		self.conn.commit()
		return view()
		

	def search(self,title="",author="",year="",isbn=""):
		self.curr.execute("select * from BOOK where Title=? or Author=? or Year=? or ISBN=?",(title,author,year,isbn))
		rows=self.curr.fetchall()
		self.conn.commit()
		return rows

	def delete(self,id):
		self.curr.execute("delete from BOOK where Id=?",(id,))
		self.conn.commit()
		return view()

	def update(self,id,title,author,year,isbn):
		self.curr.execute("update BOOK set Title=?,Author=?,Year=?,ISBN=? where Id=?",(title,author,year,isbn,id))
		self.conn.commit()
		return view()
		
	def __del__(self):
		self.conn.close()