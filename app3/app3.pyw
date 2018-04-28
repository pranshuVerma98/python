import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts" 
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]
final_list=[redirect +""+i for i in website_list]
final_string_block='\n'.join(final_list)

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,0)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23):
			print("Working time...")
			with open(hosts_path,'r+') as file:
				content=file.read()
				for website in website_list:
					if website in content:
						pass
					else:
						file.write(redirect+" "+website+"\n")
	else:
		print("Fun Time:")
		with open(hosts_path,"r+") as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()   #it will delete everything written below these lines
	time.sleep(5)