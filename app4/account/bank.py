class Account:
"""
this is document of class access by acc.__doc__() function
"""
	def __init__(self,file):
		self.file=file
		with open(self.file,'r') as f:
			self.balance=int(f.read())
	def withdraw(self,amount):
		self.balance=self.balance - amount
		
	def deposite(self,amount):
		self.balance=self.balance + amount
			
	def commit(self):
		with open(self.file,'w') as f:
			f.write(str(self.balance))
class checking(Account):
	type="check"
	def __init__(self,file,fee):
		self.fee=fee
		Account.__init__(self,file)
	def transfer(self,amount):
		self.balance=self.balance - amount-self.fee

ck=checking("balance.txt",50)
ck.transfer(101)
ck.commit()
print(ck.balance)	