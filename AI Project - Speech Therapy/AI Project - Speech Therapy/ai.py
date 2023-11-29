""" import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
flag=1
count=0
while(flag):
    with sr.Microphone() as source:
        print("speak now!")
        audio=r3.listen(source)
        print("captured")
    get=r2.recognize_google(audio)
    print(get)
    if(get=="hello"):
        print(get)
        print('count ',count)
        flag=0
    else:
        count=count+1

'''import pyttsx3

speech=pyttsx3.init()
speech.say("Hello there!")
speech.runAndWait()'''

#for greeting the person

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#getting the image using the dataset
data="love"
p=data+".png"
#img = PhotoImage(file=p) """


import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()
speech=pyttsx3.init()
global root
root=Tk()
def speaknow():
    speech.say(now)
    speech.runAndWait()

def next_word():
    now=next(data)
    #root.destroy()
    word(now)

def check():
    with sr.Microphone() as source:
        audio=r1.listen(source)
    get=r2.recognize_google(audio)
    print(get)
    if(get==now):
        print("yes")
        next_word()


def word(data):
    root=tk.Tk()
    root.title("image")
    root.geometry("600x300")
    dat=data+".png"
    pic=Image.open(dat)
    pic1=Image.open("mic.png")
    pic2=Image.open("speaker.png")

    resized=pic.resize((300,150))
    converted=ImageTk.PhotoImage(resized)

    resized1=pic1.resize((50,50))
    converted1=ImageTk.PhotoImage(resized1)

    resized2=pic2.resize((50,50))
    converted2=ImageTk.PhotoImage(resized2)

    label=tk.Label(root,image=converted,width=300,height=150)
    label.pack()
    tk.Label(root,text=data,font="TimesNewroman 20",fg="black").pack()#.place(x=300,y=200)
    play_btn=Button(root,text="hear",compound=LEFT,image=converted1,bg="white",width=100,font="arial 14",command=speaknow)                
    play_btn.place(x=150,y=200)
    #tk.Label(root,image=converted1,width=50,height=50).place(x=150,y=200)
    play_btn1=Button(root,text="say",compound=LEFT,image=converted2,bg="white",width=100,font="arial 14",command=check)                
    play_btn1.place(x=400,y=200)
    #tk.Label(root,image=converted2,width=50,height=50).place(x=400,y=200)
    Button(root,text="End Session",font="TimesNewroman 10",fg="black",command=root.quit).place(x=300,y=250)
    root.mainloop()

global data
global now
data=["love","love"]
data=iter(data)
now=next(data)
word(now)
""" for data in("love","dress"):
    word(data) """