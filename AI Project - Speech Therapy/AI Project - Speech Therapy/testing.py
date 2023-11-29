import random
words3=[]
words4=[]
words5=[]

with open('words.txt','r') as file2:
    for line in file2:
        new_line=line.replace("\n","").strip()
        if(len(new_line)==3):
            words3.append(new_line)
        elif(len(new_line)==4):
            words4.append(new_line)
        else:
            words5.append(new_line)

#print(words3)
""" print(words4)
print(words5) """

#age=int(input("Enter your age: "))
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
""" for i in w3:
    #print(w3[i])
    dataset.append(words3[i])

for j in w4:
    dataset.append(words4[j])

for k in w5:
    dataset.append(words5[k])

iterate=iter(dataset)  """
""" print(dataset)
print(type(iterate)) """

""" try:
    while(iterate):
      #p="\"
      pic="images\\"+str(next(iterate))+".png"
      print(pic) 
    #third = next(it) 
except StopIteration: 
    print("THE END")
 """

import tkinter 
from tkinter import *

root=Tk()
root.geometry("1400x700")
root.resizable(FALSE,FALSE)
redoList=["car","eat","book"]
dataset=["a","b","c","d","e","f","g","h"]

report=Frame(root)
report.pack(fill="both",expand=1)
upper=Frame(report,bg="#14A7DD",width=1400,height=130)
upper.place(x=0,y=0)
Label(upper,text="REPORT",font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=600,y=35)
""" Label(report,text="Words cracked",font="TimesNewroman 40 bold").place(x=700,y=220,anchor=CENTER)
score=str(len(dataset)-len(redoList))+"/"+str(len(dataset))
Label(report,text=score,font="TimesNewroman 20 bold",width="700",fg="white").place(x=0,y=270) """
if(redoList):
    Label(report,text="SKIPPED WORDS",font="TimesNewroman 25").place(x=570,y=300)
    xaxis,yaxis=700,390
    for l in redoList:
        yaxis=yaxis+30
        Label(report,text=l,font="TimesNewroman 15").place(x=xaxis,y=yaxis,anchor=CENTER)

root.mainloop()
