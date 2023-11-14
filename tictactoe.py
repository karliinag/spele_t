from itertools import count
from tkinter import*
from tkinter import messagebox
from tkinter import font
from turtle import width #paziņojumi, ieteikumi
mansLogs=Tk()#loga objekts
mansLogs.title("TicTacToe")

def btnClick(button): #padod visu pogai
    global speletajsX,count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==""and speletajsX==True: #spēle x spēlētājs
        button["text"]="X"#maina uz x
        speletajsX=False
        count+=1 #palielina rūtiņu skaitu

#pogu izveidošana
btn1=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn2=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn3=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn4=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn5=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn6=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn7=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn8=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))
btn9=Button(mansLogs,text="",width=6,height=3,font=("Helvica,24"))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)



mansLogs.mainloop()