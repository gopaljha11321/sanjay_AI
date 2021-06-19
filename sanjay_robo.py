import speech_recognition as sr   # voice recognition library
import random                     # to choose random words from list
import pyttsx3                    # offline Text to Speech
import datetime                   # to get date and time
import webbrowser                 # to open and perform web tasks
import serial                     # for serial communication
import pywhatkit                  # for more web automation
import subprocess
import time
import os
# Declare robot name (Wake-Up word)
robot_name = 'sanjay'
time=time.strftime("%I:%M %p")
date=datetime.date.today()
hi_words = ['hi', 'hello', 'yo baby', 'radhe radhe', 'hai']
bye_words = ['bye', 'tata', 'hasta la vista']
r_u_there = ['are you there', 'you there']
# initilize things
engine = pyttsx3.init()                    # init text to speech engine
#voices = engine.getProperty('voices')      #check for voices
#engine.setProperty('voice', voices[1].id)  # female voice
listener = sr.Recognizer()  
# initialize speech recognition API
# connect with NiNi motorcan't find '__main__' module in '' driver board over serial communication
try:
   port = serial.Serial("COM7", 9600)
   print("Phycial body, connected.")

except:
   print("Unable to connect to my physical body")
def listen():
	try:
		with sr.Microphone() as source:
			talk("How can I help you sir")
			                                      # get input from mic
			print("Talk>>")
			voice = listener.listen(source)                     # listen from microphone
			command = listener.recognize_google(voice).lower()  # use google API
			# all words lowercase- so that we can process easily
			#command = command.lower()         
			print(command)
			# look for wake up word in the beginning
			if (command.split(' ')[0] == robot_name):
				# if wake up word found....
				print("[wake-up word found]")
				process(command)     
			elif command in hi_words:
				talk("Haare krishna") 
				port.write(b'h')
			elif(command.split(' ')[0] == 'my') and (command.split(' ')[1] == 'number'):
				port.write(b'u') 
				talk("8745977703")

			elif(command.split(' ')[0] == 'rotate') and (command.split(' ')[1] == 'hand'):
				port.write(b'w') 
				talk("ok boss")
			elif(command.split(' ')[0] == 'shut') and (command.split(' ')[1] == 'up'):
				port.write(b'x') 
				talk("ok boss , sorry for disturbing you ")
			elif(command.split(' ')[0] == 'rotate') and (command.split(' ')[1] == 'head'):
				port.write(b'x') 
				talk("ok boss")
			elif (command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'my') and (command.split(' ')[2] == 'github'):
				port.write(b'u')
				talk("ok boss ")
				url1="https://github.com/gopaljha11321?tab=repositories"
				webbrowser.open(url1)                                              # read from result             
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'chrome'):
				port.write(b'u')
				subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe') 
				talk("ok boss")
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'matlab'):
				port.write(b'u')
				subprocess.call('C://Program Files//scilab-6.1.0//bin//WScilex.exe') 
				talk("ok boss")
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'file'):
				port.write(b'u')
				os.system("explorer")
				talk("ok boss , opening file explorer")
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'world'):
				port.write(b'u')
				subprocess.call('C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE') 
				talk("ok boss")
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'id'):
				port.write(b'u')
				subprocess.call('C://Program Files (x86)//Arduino//arduino.exe') 
				talk("ok boss")
			elif(command.split(' ')[0] == 'nothing'):
				port.write(b'u')
				talk("ok sir")
			elif(command.split(' ')[0] == 'date'):
				port.write(b'w')
				talk(date)
				print(date)
			elif(command.split(' ')[0] == 'time'):
				port.write(b'w')
				talk(time)
				print(time)
			elif(command.split(' ')[0] == 'open') and (command.split(' ')[1] == 'calculator'):
				port.write(b'u')
				subprocess.call('calc.exe') 
				talk("ok boss")

			elif(command.split(' ')[0] == 'who') and (command.split(' ')[1] == 'are') and (command.split(' ')[2] == 'you') :
				port.write(b'w') 
				talk("I am sanjay robotic  AI created by gopal jha robo robo i am sanjay robo")
			elif(command.split(' ')[0] == 'i') and (command.split(' ')[1] == 'am') and (command.split(' ')[2] == 'happy') :
				port.write(b'w') 
				talk("me to sir , today is the happiest day of my life , boss")
				                                               
			elif(command.split(' ')[0] != robot_name):
				talk("I Cant Understand Sir")
	except:
		pass
def process(words):
	""" process what user says and take actions """
	print(words) # check if it received any command
	# break words in
	word_list = words.split(' ')[1:]   # split by space and ignore the wake-up word
	if (len(word_list)==1):
		if (word_list[0] == robot_name):
		    talk("How Can I help you?")
		    #.write(b'l')
		    return
	if word_list[0] == 'play':
		"""if command for playing things, play from youtube"""
		talk("Okay boss, playing")
		extension = ' '.join(word_list[1:])                    # search without the command word
		port.write(b'u')
		pywhatkit.playonyt(extension)   
		port.write(b'l')          
		return
	elif word_list[0] == 'search':
		"""if command for google search"""
		port.write(b'u')
		talk("Okay boss, searching")
		port.write(b'l')
		extension = ' '.join(word_list[1:])
		pywhatkit.search(extension)
		return
	elif word_list[0] == 'where':
		"""if command for google search"""
		port.write(b'u')
		talk("I am in your heart sir")
		port.write(b'l')
		return
	if (word_list[0] == 'get') and (word_list[1] == 'info'):
		"""if command for getting info"""
		port.write(b'u')
		talk("Okay, I am right on it")
		port.write(b'u')
		extension = ' '.join(word_list[2:])                    # search without the command words
		inf = pywhatkit.info(extension)
		talk(inf)                                              # read from result             
		return
	if (word_list[0] == 'who') and (word_list[1] == 'created'):
		"""if command for getting info"""
		port.write(b'u')
		talk("gopal Jha create me  I like to work with gopal jha ")
	if (word_list[0] == 'who') and (word_list[1] == 'is'):

		"""if command for getting info"""
		port.write(b'')
		talk("gopal jha create me he is a ece student whom get diploma in ece and pursuing btech he like He like to study in robotics and automation  ")

	elif (word_list[0] == 'my') and (word_list[1] == 'number'):
		"""if command for getting info"""
		port.write(b'u')
		talk("8745977703")                                              # read from result             
		return
	elif (word_list[0] == 'open') and (word_list[1] == 'my') and (word_list[2] == 'site'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss ")
		url1="https://gopaljha11321.wixsite.com/gopaljha"
		webbrowser.open(url1)                                              # read from result             
		return
	elif (word_list[0] == 'open') and (word_list[1] == 'my') and (word_list[2] == 'channel'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss ")
		url1="https://www.youtube.com/channel/UCFQoBrQOuTbjh6nfK_8zCBQ"
		webbrowser.open(url1)
	elif (word_list[0] == 'open') and (word_list[1] == 'youtube'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss ")
		url1="https://www.youtube.com"
		webbrowser.open(url1)                                              # read from result             
		return
	elif (word_list[0] == 'open') and (word_list[1] == 'whatsapp'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss , opening whatsapp ")
		url1="https://web.whatsapp.com/"
		webbrowser.open(url1)                                              # read from result             
		return
	elif (word_list[0] == 'open') and (word_list[1] == 'facebook'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss , opening facebook ")
		url1="https://www.facebook.com/"
		webbrowser.open(url1)                                              # read from result             
		return
	elif (word_list[0] == 'open') and (word_list[1] == 'my') and (word_list[2] == 'project'):
		"""if command for getting info"""
		port.write(b'u')
		talk("ok boss ")
		url1="https://gopaljha11321.github.io/fp_Vitality/"
		webbrowser.open(url1)                                              # read from result             
		return
	elif word_list[0] == 'open':
		"""if command for opening URLs"""
		port.write(b'l')
		talk("Opening, sir")
		url = f"http://{''.join(word_list[1:])}"   # make the URL
		webbrowser.open(url)
		return
	elif word_list[0] == 'uppercut':
		port.write(b'U')
	elif word_list[0] == 'confuse':
		port.write(b's')
	elif word_list[0] == 'punch':
		port.write(b'p')
   # now check for matches
	for word in word_list:
		if word in hi_words:
			""" if user says hi/hello greet him accordingly"""
			port.write(b'h')               # send command to wave hand
			talk(random.choice(hi_words))
		elif word in bye_words:
			""" if user says bye etc"""
			talk(random.choice(bye_words))
def talk(sentence):
	""" talk / respond to the user """
	engine.say(sentence)
	engine.runAndWait()
# run the app
while True:
   listen()