from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
from tkinter import messagebox
import random
import string

#dataset
words3=[]
words4=[]
words5=[]
global dataset
global data
global pic
global dataset1
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
age=3
if(age==3):
    w3=random.sample(range(0, 10), 2)
    #w4=random.sample(range(0, 10), 3)
    #w5=random.sample(range(0, 10), 2)
elif(age==4):
    w3=random.sample(range(0, 10), 3)
    w4=random.sample(range(0, 10), 5)
    w5=random.sample(range(0, 10), 2)
else:
    w3=random.sample(range(0, 10), 2)
    w4=random.sample(range(0, 10), 3)
    w5=random.sample(range(0, 10), 5)

#dataset creation
dataset=[]
for i in w3:
    dataset.append(words3[i])

""" for j in w4:
    dataset.append(words4[j])

for k in w5:
    dataset.append(words5[k]) """

# dataset initializing
realDataset=dataset
dataset1=iter(dataset)

# return the data
def getData():
    global data
    data=next(dataset1)

""" def get_redodata():
    global data
    data=next(redo_dataset1) """

# initialize the instances for conversion
r1=sr.Recognizer()
r2=sr.Recognizer()
speech=pyttsx3.init()

# Create an instance of tkinter frame or window
root = Tk()
root.geometry("1400x700")
root.resizable(FALSE,FALSE)

#redo operations
""" def redo():
    global redoDataset
    global redo_dataset1
    redoDataset=redoList
    redoList.clear()
    redo_dataset1=iter(redoDataset)
    get_redodata()
    redo_on_click() """

# redo: text to speech
""" def redo_speaknow():
    speech.say(data)
    speech.runAndWait() """

# text to speech
def speaknow(): # passing data
    """ if(redoDataset):
        redo_speaknow()  """
    speech.say(data)
    speech.runAndWait()


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

#report page
def reportPage():
    win.pack_forget()
    report.pack(fill="both",expand=1)
    #Label(report,text="yes").pack()
    upper=Frame(report,bg="#14A7DD",width=1400,height=130)
    upper.place(x=0,y=0)
    Label(upper,text="REPORT",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)
    Label(report,text="Words cracked",font="TimesNewroman 40 bold").place(x=500,y=200)
    score=str(len(realDataset)-len(redoList))+"/"+str(len(realDataset))
    Label(report,text=score,font="TimesNewroman 20 bold",bg="green").place(x=650,y=300)
    if(redoList):
        Label(report,text="skipped words",font="TimesNewroman 15").place(x=570,y=350)
        xaxis,yaxis=650,370
        for l in redoList:
         yaxis=yaxis+30
         Label(report,text=l,font="TimesNewroman 15").place(x=xaxis,y=yaxis)

# when end session is clicked
def question():
    """ if(redoList):
        res1=messagebox.askyesno("pop","You have some words to perfect, would you like to continue?")
        if(res1):
            redo()
        else:
            reportPage() """
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

win=Frame(root)
win.pack(fill="both",expand=1)
# position the image
Label(win, text="                        ",font=('Calibri 20 bold')).grid(row=2,column=2)
Label(win, text="                      ",font=('Calibri 20 bold')).grid(row=3,column=5)
Label(win, text="                      ",font=('Calibri 20 bold')).grid(row=4,column=8)
Label(win, text="                  ",font=('Calibri 20 bold')).grid(row=5,column=10)

#First image
getData()
count=0
pic="images\\"+data+".png"

# Image
img1=ImageTk.PhotoImage(Image.open(pic))
label=Label(win,image=img1)
label.grid(row=7,column=15)
label1 = Label(win, text=data,font=('Calibri 20 bold'))
label1.place(x=700,y=427,anchor=CENTER)

# speaker button
pic1=ImageTk.PhotoImage(Image.open("speak.png"))
play_btn=Button(win,text="hear",compound=LEFT,image=pic1,width=100,font="arial 14",command=speaknow) 
play_btn.place(x=565,y=470)

# microphone button
pic2=ImageTk.PhotoImage(Image.open("microphone.png"))
play_btn1=Button(win,text="say",compound=LEFT,image=pic2,width=100,font="arial 14",command=check) 
play_btn1.place(x=730,y=470)
               
# session frame
upper=Frame(win,bg="#14A7DD",width=1400,height=130)
upper.place(x=0,y=0)
Label(upper,text="Session",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)

# End Session button
end_session=Button(win,text="End session",font="TimesNewroman 15",command=question).place(x=700,y=600,anchor=CENTER)

# report frame
report=Frame(root,width=700,height=350)


win.mainloop()

