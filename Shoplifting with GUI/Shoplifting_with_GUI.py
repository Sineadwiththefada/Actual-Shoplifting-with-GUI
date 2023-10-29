import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk,Text
import random
import time
choice=""
tab1finished =False
rootwindow1 =Tk()
rootwindow1.geometry("700x600")
rootwindow1.resizable(False,False)
text =Text(rootwindow1,height=7 ,width=100)
Font_tuple = ("New Times Roman", 11, "normal") 
text.configure(font = Font_tuple)
text.pack()
text.insert('1.0', 'You are an employee at Co-op. You see a customer wandering around the store picking up items for a long time with a big backpack. ')
time.sleep(1)
rootwindow1.quit()
mainloop()
tab1finished =True
if choice == "Go and Confront Them":
   choice = 1
elif choice == "Watch Them":
   choice= 2
elif choice == "Ask If They Need Help":
   choice=3

rootwindow = Tk()
rootwindow.geometry("500x550")
rootwindow.resizable(False, False)
text = Text(rootwindow, height=2)
text.pack()
text.insert('1.0', 'What will you do? ')
Font_tuple = ("New Times Roman", 11, "normal") 
text.configure(font = Font_tuple)
variable = StringVar(rootwindow)
variable.set('Choose your option')
choices = ['Go and Confront Them', 'Watch Them', 'Ask If They Need Help']
variable = StringVar(rootwindow)
variable.set('Choose Your Option')
w = OptionMenu(rootwindow, variable, *choices)
submit_button = ttk.Button(
rootwindow,
text='Submit',
command=lambda: rootwindow.quit()
)  

submit_button.pack(
ipadx=5,
ipady=5, 
expand=False    
)
submit_button.place(x=200, y=135)
w.pack(); rootwindow.mainloop()
choice =str(variable.get())
if choice =="Go and Confront Them":
   choice=1
elif choice == "Watch Them":
   choice=2
elif choice =="Ask If They Need Help":
   choice =3
score=0
customer = 1
score = 0
end = False
#customer types are as follows 1 is violent shoplifter 2 is normal person 3 is confused person
rootwindow.quit()
if customer ==1:
    score-=10
    tab1finished =False
    rootwindow1 =Tk()
    rootwindow1.geometry("700x600")
    rootwindow1.resizable(False,False)
    text =Text(rootwindow1,height=7 ,width=100)
    text.pack()
    text.insert('1.0', 'The customer starts to become violent ')
    Font_tuple = ("New Times Roman", 11, "normal") 
    text.configure(font = Font_tuple)
    time.sleep(1)
    rootwindow1.quit()
    mainloop()
    tab1finished =True
    rootwindow = Tk()
    rootwindow.geometry("500x550")
    rootwindow.resizable(False, False)
    text = Text(rootwindow, height=2)
    text.pack()
    text.insert('1.0', 'What will you do? ')
    Font_tuple = ("New Times Roman", 11, "normal") 
    text.configure(font = Font_tuple)
    variable = StringVar(rootwindow)
    variable.set('Choose your option')
    choices = ['Intervene Yourself', ' Ask A Colleague To Intervene And Call The Police ', 'Attempt To Call The Police Yourself']
    variable = StringVar(rootwindow)
    variable.set('Choose Your Option')
    w = OptionMenu(rootwindow, variable, *choices)
    submit_button = ttk.Button(
    rootwindow,
    text='Submit',
    command=lambda: rootwindow.quit()
     )  

    submit_button.pack(
    ipadx=5,
    ipady=5,
    expand=False    
    )
    submit_button.place(x=200, y=135)
    w.pack(); rootwindow.mainloop()
    choice =str(variable.get())
    if choice=="Intervene Yourself":
       choice=1
    elif choice =="Ask A Colleague To Intervene And Call The Police":
       choice=2
    elif choice =="Attempt To Call The Police":
       choice=3
    if choice == 1:
       tab1finished =False
rootwindow1 =Tk()
rootwindow1.geometry("800x800")
rootwindow1.resizable(False,False)
text =Text(rootwindow1,height=800 ,width=800)
text.pack()
text.insert('1.0', 'You obtain a serious injury.You endangered yourself by intervening without backup when you knew the person was violent.this is a bad idea instead try to call for backup with colleagues.')
Font_tuple = ("New Times Roman", 10, "normal") 
text.configure(font = Font_tuple)
time.sleep(1)
rootwindow1.quit()
mainloop()
tab1finished =True
rootwindow1 =Tk()
rootwindow1.geometry("900x900")
rootwindow1.resizable(False,False)
text =Text(rootwindow1,height=900 ,width=900)
text.pack()
text.insert('1.0', 'remember there are many different reasons why a customer may act suspicious.the right course of action always depends on the circumstances. if you try this simulation again you may find that your inital right actions may now be wrong for the situation."however the basic principles always apply of trying to keep yourself and other people safe first.')
Font_tuple = ("New Times Roman", 10, "normal") 
text.configure(font = Font_tuple)
time.sleep(1)
rootwindow1.quit()
mainloop()
    





