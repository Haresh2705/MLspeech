from cProfile import label
from nltk.tokenize import *
import string
from nltk.corpus import stopwords
import nltk
#print(nltk.__file__)
sentence="Happy birthday uncle Daniel. Love Heart!. i love you so much"
punctuations=string.punctuation
#print(sent_tokenize(sentence))  #tokenizes paras into sentence
words=word_tokenize(sentence)  #tokenizes sentence into words
stopword=stopwords.words("english")
sensible_words= [w for w in words if not w in (stopword and punctuations)]
pos=nltk.pos_tag(sensible_words)
#print(pos)
from nltk.stem.porter import PorterStemmer
port=PorterStemmer()
words=[port.stem(i) for i in ("love","lovingly","joyfull","joyously","happieness","happiely")]
#print(words) 

import nltk
from nltk.stem import WordNetLemmatizer
'''from nltk.corpus import sentiwordnet as swn
word=swn.senti_sysnet("happy.n.03")
#word="happy"
#print(word.pos_score())
lemmatizer=WordNetLemmatizer()
#sent="I am gonna die soon. ada ennaga neenga onnum purila"
#tok= word_tokenize(sent)
#for i in tok:
    #print(lemmatizer.lemmatize(i))
breakdown = swn.senti_synsets('breakdown','a')
print(breakdown)'''
'''nltk.download('sentiwordnet')
from sentiwordnet import SentiWordNetCorpusReader, SentiSynset
swn=SentiWordNetCorpusReader()
print(swn.senti_synset('breakdown.n.03'))'''
from nltk.corpus import sentiwordnet as swn
#print(swn.senti_synset('breakdown.n.03'))
#happy = swn.senti_synsets('happy', nltk.pos_tag('happy'))[0]
#happy0 = list(happy)[0]
#print(happy.pos_score)
from textblob import TextBlob
words=["love","movie","impressive","talent","cheers"]
'''for i in a:
  print(TextBlob(i).sentiment)
'''
def cal_ploarity(words):
    pos,neg,neu=0,0,0
    for word in words:
      sent=TextBlob(word)
      pol=sent.sentiment.polarity
      print(pol)
      '''if(pol>0):
        pos=pos+pol
      elif(pol<0):
        neg=neg+pol
      else:
        neu=neu+pol
    neg=neg*(-1)
    if(pos>neg and pos>neu):
      print("POSITIVE Sentiment")
    elif(neg>neu):
      print("NEGATIVE Sentiment")
    else:
      print("NEUTRAL Sentiment")
#cal_ploarity(words)
from textblob.classifiers import NaiveBayesClassifier
training=[('He is good','pos'),('I am bad','neg'),('I am okay','pos'),('She is nice','pos'),('Its beautiful','pos'),('He is ugly','neg'),('Its irritating','neg'),('Its sarcastic','neg'),('Its somewhat good','pos'),('Anything is not okay for me','neg')]
c=NaiveBayesClassifier(training)
print(c.classify("This is total shit"))

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()
sent="I love you but I hate you"
print(sent)
pol=sia.polarity_scores(sent)
print(pol)'''
#print(pos)
## to read train dataset
'''file=open('doc1.txt','r')
text=file.readlines()
file.close()
train_dataset=[]
train=[]
for i in text:
  sentence,polarity=i.strip().split('#')
  train_dataset.append(sentence)
  train.append(polarity)
  print(sentence)
  pol=sia.polarity_scores(sentence)
  print(pol)
  print(polarity)
print("----------------------------------------------------------------")
print("                         EMOTION DETECTOR                       ")
print("----------------------------------------------------------------")'''




import pyttsx3




#root.mainloop()

""" tts = pyttsx3.init()
voices=tts.getProperty('voices')
tts.setProperty('voice',voices[1].id)
tts.setProperty('rate',120)
#setvoice()
tts.say("Hello")
tts.runAndWait() """

'''a=["1","2","3"]
b=["Dhiv","ndj","jdhvj"]

import pandas as pd
#print(pd.DataFrame(a,b))
d=list(zip(a,b))
print(d)
'''

""" from tkinter import *
import sys
from PIL import Image, ImageTk
def quit():
  sys.exit()
ws = Tk()
ws.title('PythonGuides')
tts = pyttsx3.init()
voices=tts.getProperty('voices')
tts.setProperty('voice',voices[1].id)
tts.setProperty('rate',120)

#img = PhotoImage(file=p)

Label(
    ws,
    image=img
).pack()
def change():
  img2=ImageTk.PhotoImage(Image.open("ajith.png"))
  label.configure(image=img2)
  label.image=img2


'''Button(
    ws,
    image=img,
    command=quit
).pack()'''
img1=Image.open("love.png")
resized=img1.resize((300,250))
converted=ImageTk.PhotoImage(resized)
#Create a Label widget
img_label= Label(ws,image=converted).place(x=550,y=150)

#Create a Button to handle the update Image event
button= Button(ws, text= "Change", font= ('Helvetica 13 bold'),command= change)
button.pack()
ws.mainloop()
 """


""" from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time) """



from tkinter import *
from PIL import Image,ImageTk
import random

#dataset
words3=[]
words4=[]
words5=[]
global dataset
global data
global pic
global dataset1

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
dataset=[]
for i in w3:
    #print(w3[i])
    dataset.append(words3[i])

for j in w4:
    dataset.append(words4[j])

for k in w5:
    dataset.append(words5[k])

# tkinter interface
root=Tk()
root.title("Title")
root.iconbitmap("icon.ico")
root.geometry("1400x700")
root.resizable(FALSE,FALSE)
def change_img(data):
  pic="images\\"+data+".png"
  global img2
  img2=ImageTk.PhotoImage(Image.open(pic))
  label.configure(image=img2)
  label1.configure(text=data)

  if(dataset.index(data)==9):
    button.configure(state=DISABLED)
    #root.quit()

  """  try:
    while(dataset):
      data=next(dataset)
      pic="images\\"+data+".png"
      img2=ImageTk.PhotoImage(Image.open(pic))
      label.configure(image=img2)
      label.image=img2
      label1.configure(text=data)
   except StopIteration: 
    print("end") """
   


# data initializing
dataset1=iter(dataset)
data=next(dataset1)
pic="images\\"+data+".png"


""" img1=Image.open("love.png")
resized=img1.resize((300,250))
converted=ImageTk.PhotoImage(resized)
#Create a Label widget
#global img_label
img_label= Label(root,image=converted).place(x=550,y=150) """

#session frame
upper=Frame(root,bg="#14A7DD",width=1400,height=130)
upper.place(x=0,y=0)
Label(upper,text="Session",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)

#space for image positioning
Label(root, text="                        ",font=('Calibri 18 bold'),bg="#14A7DD").grid(row=2,column=2)
Label(root, text="                      ",font=('Calibri 18 bold'),bg="#14A7DD").grid(row=3,column=5)
Label(root, text="                      ",font=('Calibri 18 bold'),bg="#14A7DD").grid(row=4,column=8)
Label(root, text="                  ",font=('Calibri 12 bold'),bg="#14A7DD").grid(row=5,column=10)
Label(root, text="                        ",font=('Calibri 12 bold')).grid(row=7,column=20)
#Label(root, text="                  ",font=('Calibri 12 bold'),bg="#14A7DD").grid(row=5,column=10)

#open image
img1= ImageTk.PhotoImage(Image.open(pic))

#Create a Label for image
label= Label(root,image= img1)
label.grid(row=15,column=25)

label1 = Label(root, text=data,font=('Calibri 20 bold'))
label1.place(x=700,y=430,anchor=CENTER)
#Create a Button to handle the update Image event
button= Button(root, text= "Change", font= ('Helvetica 13 bold'),
command=lambda:change_img(next(dataset1)))
button.place(x=650,y=600)

#win.bind("<Return>", change_img)
root.mainloop()
