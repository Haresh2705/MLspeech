import tkinter as tk
from tkinter import *
import speech_recognition as sr
import pyttsx3
from PIL import Image,ImageTk

#import time
r1=sr.Recognizer()
r2=sr.Recognizer()

root=Tk()
root.title("Speech Therapy")
root.geometry("1000x580+200+80")
root.resizable(False,False) #True,True
root.configure(bg="#F7AC40")
#root.mainloop()
""" logo=PhotoImage(file="love.png") #not needed
Label(root,image=logo,bg="#F7AC40").place(x=880,y=530) """

upper_frame=Frame(root,bg="#14A7DD",width=1200,height=130)
upper_frame.place(x=0,y=0)
""" pic=PhotoImage(file="mic.png") #resize the image
Label(upper_frame,image=pic,bg="#14A7DD").place(x=150,y=20) """

tts=pyttsx3.init()
global top

def new_window():
    root.destroy()
    global img
    top=tk.Tk()
    top.title("Second window")
    img=Image.open("love.png")
    rimg=img.resize((300,150),Image.ANTIALIAS)
    convert=ImageTk.PhotoImage(rimg)
    label=tk.Label(top,image=convert,width=300,height=150)
    label.pack()
    top.mainloop()
    

def speaknow():
    text=text_box.get(1.0,END)
    name=text_box1.get(1.0,END)
    age=int(text_box2.get(1.0,END))
    tts.say(text)
    tts.say("you're turn")
    tts.runAndWait()
    with sr.Microphone() as source:
        audio=r1.listen(source)
    get=r2.recognize_google(audio)
    print(get)
    if(get==text):
        tts.say("Success")
        tts.runAndWait()
    print(name)
    print(type(age))
    new_window()
    


Label(upper_frame,text="Speech Therapy",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=250,y=35)
text_box=Text(root,font="calibri 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
text_box.place(x=30,y=150,width=940,height=180)
text_box1=Text(root,font="calibri 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
text_box1.place(x=340,y=400,width=80,height=30) #change sizze
text_box2=Text(root,font="calibri 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
text_box2.place(x=540,y=400,width=80,height=30) #resize
Label(root,text="name",font="TimesNewroman 15 bold",bg="#F7AC40",fg="white").place(x=340,y=370)
Label(root,text="age",font="TimesNewroman 15 bold",bg="#F7AC40",fg="white").place(x=540,y=370)
play_button=PhotoImage(file="mic.png")
play_btn=Button(root,text="speak",compound=LEFT,image=play_button,bg="white",width=130,font="arial 14 bold",borderwidth='0.1c',command=speaknow)                
play_btn.place(x=435,y=450)
root.mainloop()


""" 
#to quit the program
button_quit=Button(root,text="ok",command=root.quit)
button_quit.pack() """