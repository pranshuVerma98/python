import json
from difflib import SequenceMatcher
from difflib import get_close_matches
import speech_recognition as sr  
import pyttsx

data=json.load(open("data.json"))
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source) 	
 

def find_mean(word):
	word=word.lower()
	if word in data:
		mean=data[word]
		return mean
	elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
		word=word.title()
		return data[word]
	elif word.upper() in data: #in case user enters words like USA or NATO
		word=word.upper()
		return data[word]
	else:
		try:
			mean=get_close_matches(word,data.keys())[0]
			w=input("You Mean To that:"+str(mean)+"?? 'Y' for Yes and 'N' for No:  ")
			if w.lower() == 'y':
				return data[mean]
			else:
				return "Sorry!! Try Again.. May be its not exit"
		except:
			return "Words Not Exist"	
#code is return here
word=r.recognize_google(audio)
mean=find_mean(word)
if type(mean)==list:
		for i in mean :
			print(i)
			engine = pyttsx.init()
			engine.say("Meanings Are as  " +i)
			engine.runAndWait()
else:
		print(mean)
		engine = pyttsx.init()
		engine.say("Meaning is  " +mean)
		engine.runAndWait()
		
