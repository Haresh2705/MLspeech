from tkinter import *
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
from PIL import Image,ImageTk
from datetime import datetime
import time
import string
import random

r1=sr.Recognizer()
r2=sr.Recognizer()
speech = pyttsx3.init()
voices=speech.getProperty('voices')
speech.setProperty('voice',voices[1].id)
speech.setProperty('rate',120)

#dataset
words3=[]
words4=[]
words5=[]
""" global dataset
global data
global pic
global dataset1 """
global redoList
global count
count=0
redoList=[]

# read the words from the txt file
with open('words.txt','r') as file2:
    for line in file2:
        new_line=line.replace("\n","").strip()
        if(len(new_line)==3):
            words3.append(new_line)
        elif(len(new_line)==4):
            words4.append(new_line)
        else:
            words5.append(new_line)

#generate the random numbers for the dataset

def create_dataset(age):
    if(age==3):
        w3=random.sample(range(0, 10), 5)
        w4=random.sample(range(0, 10), 3)
        w5=random.sample(range(0, 10), 2)
    elif(age==4):
        w3=random.sample(range(0, 10), 3)
        w4=random.sample(range(0, 10), 5)
        w5=random.sample(range(0, 10), 2)
    else:
        w3=random.sample(range(0, 10), 2)
        w4=random.sample(range(0, 10), 3)
        w5=random.sample(range(0, 10), 5)

    #dataset creation
    global dataset
    dataset=[]
    for i in w3:
        dataset.append(words3[i])

    """ for j in w4:
        dataset.append(words4[j])

    for k in w5:
        dataset.append(words5[k]) """

    # dataset initializing
    global realDataset
    global dataset1
    realDataset=dataset
    dataset1=iter(dataset)

# return the data
def getData():
    global data
    data=next(dataset1)

# tkinter interface
root=Tk()
root.geometry("1400x700")
#root.geometry("500x500")
root.resizable(False,False)
root.title("Speech Therapy")
root.iconbitmap("icon.ico")

# text to speech
def speaknow(): # passing data
    for i in range(3):
        speech.say(data)
        speech.runAndWait()
        time.sleep(1)

# speech to text
def check():
    with sr.Microphone() as source:
        audio=r1.listen(source)
    try:   
        get=r2.recognize_google(audio)
        get=get.lower()
        print(get)
        if(get==data):
            print("yes")
            #getData()
            if(dataset.index(data)==(len(dataset)-1)):
                print(redoList)
                speech.say("Session is complete")
                speech.runAndWait()
            else:
                on_click()
        else:
            
            global count
            count=count+1                 #wrong pronounce
            if(count==3):
                redoList.append(data)
                if(dataset.index(data)==(len(dataset)-1)):
                    speech.say("Session will be ending here..")
                    speech.runAndWait()
                else:
                    speech.say("Let's move to next one")
                    speech.runAndWait()
                    on_click()
            else:
                speech.say("Try again")
                speech.runAndWait()
    except sr.UnknownValueError:
        speech.say("Not captured")
        speech.runAndWait()

# Change the image and the text
def on_click():   
   getData()
   count=0
   picture="images\\"+data+".png" 
   global img2
   img2=ImageTk.PhotoImage(Image.open(picture))
   label.configure(image=img2)
   label.image=img2
   label1.configure(text=data)

# pop-up message before moving on to report
def question():
    
    if(dataset.index(data)==(len(dataset)-1)):
        reportPage()
    else:
        res=messagebox.askyesno("pop","Are you sure, You want to quit?") 
        #askquestion - yes or no
        #askyesno - 1 or 0
        if(res):
            #win.destroy()
            #win.pack_forget()
            root.quit()

#hide all frames
def hide():
    main_page.pack_forget()
    session_page.pack_forget()
    report_page.pack_forget()

# session frame
def session():
    hide()
    session_page.pack(fill="both",expand=1)
    
    # position the image
    Label(session_page, text="                        ",font=('Calibri 20 bold')).grid(row=2,column=2)
    Label(session_page, text="                      ",font=('Calibri 20 bold')).grid(row=3,column=5)
    Label(session_page, text="                      ",font=('Calibri 20 bold')).grid(row=4,column=8)
    Label(session_page, text="                  ",font=('Calibri 20 bold')).grid(row=5,column=10)
    
    #First image
    getData()
    global count
    count=0
    pic="images\\"+data+".png"

    # Image
    global img1
    img1=ImageTk.PhotoImage(Image.open(pic))
    global label
    global label1
    label=Label(session_page,image=img1)
    label.grid(row=7,column=15)
    label1 = Label(session_page, text=data,font=('Calibri 20 bold'))
    label1.place(x=700,y=427,anchor=CENTER)

    # speaker button
    global pic1
    pic1=ImageTk.PhotoImage(Image.open("speak.png"))
    play_btn=Button(session_page,text="hear",compound=LEFT,image=pic1,width=100,font="arial 14",command=speaknow) 
    play_btn.place(x=565,y=470)

    # microphone button
    global pic2
    pic2=ImageTk.PhotoImage(Image.open("microphone.png"))
    play_btn1=Button(session_page,text="say",compound=LEFT,image=pic2,width=100,font="arial 14",command=check) 
    play_btn1.place(x=730,y=470)

    #session frame
    upper=Frame(session_page,bg="#14A7DD",width=1400,height=130)
    upper.place(x=0,y=0)
    Label(upper,text="Session",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)

    # End Session button
    end_session=Button(session_page,text="End session",font="TimesNewroman 15",command=question).place(x=700,y=600,anchor=CENTER)


# report frame
def reportPage():
    session_page.pack_forget()
    report_page.pack(fill="both",expand=1)
    upper=Frame(report_page,bg="#14A7DD",width=1400,height=130)
    upper.place(x=0,y=0)
    Label(upper,text="REPORT",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)
    Label(report_page,text="Words cracked",font="TimesNewroman 40 bold").place(x=700,y=220,anchor=CENTER)
    score=str(len(realDataset)-len(redoList))+"/"+str(len(realDataset))
    Label(report_page,text=score,font="TimesNewroman 20 bold",bg="green").place(x=670,y=270)
    if(redoList):
        Label(report_page,text="SKIPPED WORDS",font="TimesNewroman 25").place(x=570,y=350)
        xaxis,yaxis=700,390
        for l in redoList:
         yaxis=yaxis+30
         Label(report_page,text=l,font="TimesNewroman 15").place(x=xaxis,y=yaxis)

def start_session():
    global name
    global age
    name=name_var.get()
    age=int(age_var.get())
    create_dataset(age)

    now = datetime.now()
    current_time = int(now.strftime("%H"))
    if(current_time>= 0 and current_time<12):
        greet="good morning"
    elif(current_time>=12 and current_time<18):
        greet="good afternoon"
    else:
        greet="good evening"
    
    intro=greet+name
    speech.say(intro)
    speech.runAndWait()
    speech.say("Let's start the session")
    speech.runAndWait()
    session()


# frame declaration
main_page=Frame(root,width=1000,height=1000)
session_page=Frame(root,width=1000,height=1000)
report_page=Frame(root,width=1000,height=1000)

name_var=tk.StringVar()
age_var=tk.StringVar()

#main frame
main_page.pack(fill="both",expand=1)
main_page.configure(bg="white")
upper_frame=Frame(main_page,bg="#14A7DD",width=1400,height=130)
upper_frame.place(x=0,y=0)
Label(upper_frame,text="Speech Therapy",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=500,y=35)

#get name and age
name_label = tk.Label(main_page, text = "Name", font="TimesNewroman 20 normal",bg="white").place(x=550,y=250)
Entry(main_page,textvariable=name_var,font="TimesNewroman 20 normal").place(x=550,y=300,width=300,height=30)
age_label = tk.Label(main_page, text = "Age", font="TimeNewroman 20 normal",bg="white").place(x=550,y=350)
Entry(main_page,textvariable=age_var,font="TimeNewroman 20 normal").place(x=550,y=400,width=300,height=30)
main_page_button=Button(main_page,text="Start session",font="TimesNewroman 15",command=start_session).place(x=700,y=500,width=200,height=30,anchor=CENTER)

root.mainloop()