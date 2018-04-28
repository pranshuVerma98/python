"""
this is a documentation....
"""
#this is a file programmed
'''file=open("new 2.txt",'r')
conn=file.readlines()
conn=[i.rstrip("\n") for i in conn ]
print(conn)
file.close()
file=open("new 2.txt",'w')
text="hello this is a new file...\n created by me \n Tony stark"
file.write(text)
file.close()

file=open("new 2.txt",'a')
text="hello this is a current file...\n created by me \n Tony stark \n this is extra text above 4 line"
file.write(text)
file.close()
'''

with open("new 2.txt",'r+') as file:
	file.seek(0)
	#file.write("its with text")
	conn=file.read()
	print(conn)