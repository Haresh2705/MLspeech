import speech_recognition as sr
import pyttsx3
import sys
from tkinter import *

r1=sr.Recognizer()
r2=sr.Recognizer()
speech=pyttsx3.init()
speech.setProperty('rate',120)
voices=speech.getProperty('voices')
speech.setProperty('voice',voices[1].id)

dataset =["hello"]
attempts=[]
redo=[]
rattempts=[]
pics=["love.png"]

ws = Tk()
ws.title('PythonGuides')

""" with open('AI project\img_file_paths.txt','r') as file2:
    for line in file2:
        new_line=line.replace("\n","").strip()
        pics.append(new_line)  """
#text to speech
for data in dataset:
    """ img = PhotoImage(file=pics[0])
    Label(
    ws,
    image=img
    ).pack() """
    

    for i in range(1):      
        speech.say(data)
        speech.runAndWait()
    
    speech.say("You're turn now")
    speech.runAndWait()

#speech to text
    flag=1
    count=0
    while(flag):
        with sr.Microphone() as source:
            print("speak now!")
            audio=r1.listen(source)
            print("captured")
        get=r2.recognize_google(audio)
        print(get)
        if(get==data):
            #print(get)
            attempts.append(count)
            print('count ',count)
            flag=0
        else:
            speech.say("Couldn't get you")
            speech.runAndWait()
            count=count+1
            if(count>2):
                redo.append(data)
                #del dataset[]
                break
    
    if(count>2):
        break    
    
  
""" print("Would you like to continue?(yes/end)")
choice=input()
if(choice=="end"):
    sys.exit()
else:
    if(redo):
    therapy(redo) """


ws.mainloop()