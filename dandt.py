"""
import datetime
import time
now=datetime.datetime.now()
yes=datetime.datetime(2018,1,1,0,0,0)
delta=yes-now
print(str(delta))
time.sleep(6)
print("next line ")
"""
"""" This is another example of diclaring above code :::: """
from datetime import datetime,timedelta
now = datetime.now()
print ("Now: ", now)
print ("Today's date: ", now.strftime('%Y-%m-%d')) 
print ("year:", now.year)
print ("month:", now.month)
print ("day:", now.day)
print ("hour:", now.hour)
print ("minute:", now.minute)
print ("second:", now.second)
after=now+timedelta(days=2)
print("new date",after)