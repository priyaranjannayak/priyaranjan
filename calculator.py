import tkinter
from tkinter import*
from tkinter import messagebox
val=""
A=0
opperator=""





def btn_7_isclicked():
    global val
    val=val+"7"
    data.set(val)

def btn_8_isclicked():
    global val
    val=val+"8"
    data.set(val)

def btn_9_isclicked():
    global val
    val=val+"9"
    data.set(val)
def btn_1_isclicked():
    global val
    val=val+"1"
    data.set(val)
def btn_2_isclicked():
    global val
    val=val+"2"
    data.set(val)
def btn_3_isclicked():
    global val
    val=val+"3"
    data.set(val)
def btn_4_isclicked():
    global val
    val=val+"4"
    data.set(val)
def btn_5_isclicked():
    global val
    val=val+"5"
    data.set(val)
def btn_6_isclicked():
    global val
    val=val+"6"
    data.set(val)
    

def btn_0_isclicked():
    global val
    val=val+"0"
    data.set(val)
    
def btn_dot_isclicked():
    global val
    val=val+"."
    data.set(val)
    
    
    
    
    
    
    
    
    
    
def btn_puls_isclicked():
    global A
    global opperator
    global val
    if val=="":
        val="+"
        data.set(val)
        val=str(val)
    else:
        opperator="+"
        val=str(val)
        val=val +"+"
        data.set(val)
        
    
    
    
    
def btn_diif_isclicked():
    global A
    global opperator
    global val
    if val=="":
        val="-"
        data.set(val)
        val=str(val)
    else:
        opperator="-"
        val=str(val)
        val=val +"-"
        data.set(val)
        
          
    
        
  
            
    

def c_pressed():
    global A
    global opperator
    global val
    A=0
    opperator=""
    val=""
    data.set(val)
def btn_mult_isclicked():
    global A
    global opperator
    global val
    opperator="*"
    val=str(val)
    val=val +"*"
    data.set(val)
    val=str(val)
    
    
def btn_division_isclicked():
    global A
    global opperator
    global val
    opperator="/"
    val=str(val)
    val=val +"/"
    data.set(val)

def btn_percn_isclicked():
    global A
    global val
    A=int(val)
    val=A/100
    data.set(val)    
def ruselt():
    global A
    global opperator
    global val
    val=eval(val)
    data.set(val)
       
            
def back():
    global A
    global opperator
    global val
    x=str(val)
    val2=list(x)
    val2.pop(-1)
    val="".join(val2)
    data.set(val)
    
     
        
    




    
    
    
win=tkinter.Tk()
win.geometry("380x490+400+200")
win.resizable(0,0)
win.title("MY CALCULATER")


data=StringVar()


lbl= Label(win,text="lebel",font=('algerian',20),anchor="se",textvariable=data,background="#ffffff",fg="#000000")
lbl.pack(expand ="true",fill='both')

btnrow1= Frame(win)
btnrow1.pack(expand = "true",fill ='both')

btnrow2= Frame(win)
btnrow2.pack(expand = "true",fill ='both')

btnrow3= Frame(win)
btnrow3.pack(expand = "true",fill ='both')

btnrow4= Frame(win)
btnrow4.pack(expand = "true",fill ='both')

btnrow5= Frame(win)
btnrow5.pack(expand = "true",fill ='both')



btn1=Button(btnrow1,text="c",font=('algerian',20),relief=GROOVE,border=0,command=c_pressed)
btn1.pack(side='left',expand='true',fill='both')

btn2=Button(btnrow1,text="⌫",font=('algerian',20),relief=GROOVE,border=0,command=back)
btn2.pack(side='left',expand='true',fill='both')

btn3=Button(btnrow1,text="x",font=('algerian',20),relief=GROOVE,border=0,command=btn_mult_isclicked)
btn3.pack(side='left',expand='true',fill='both')

btn4=Button(btnrow1,text="/",font=('algerian',25),relief=GROOVE,border=0,command=btn_division_isclicked)
btn4.pack(side='left',expand='true',fill='both')





btn1=Button(btnrow2,text="7",font=('algerian',20),relief=GROOVE,border=0,command=btn_7_isclicked)
btn1.pack(side='left',expand='true',fill='both')

btn2=Button(btnrow2,text="8",font=('algerian',20),relief=GROOVE,border=0,command=btn_8_isclicked)
btn2.pack(side='left',expand='true',fill='both')

btn3=Button(btnrow2,text="9",font=('algerian',20),relief=GROOVE,border=0,command=btn_9_isclicked)
btn3.pack(side='left',expand='true',fill='both')

btn4=Button(btnrow2,text="+",font=('algerian',25),relief=GROOVE,border=0,command=btn_puls_isclicked)
btn4.pack(side='left',expand='true',fill='both')




btn1=Button(btnrow3,text="4",font=('algerian',20),relief=GROOVE,border=0,command=btn_4_isclicked)
btn1.pack(side='left',expand='true',fill='both')

btn2=Button(btnrow3,text="5",font=('algerian',20),relief=GROOVE,border=0,command=btn_5_isclicked)
btn2.pack(side='left',expand='true',fill='both')

btn3=Button(btnrow3,text="6",font=('algerian',20),relief=GROOVE,border=0,command=btn_6_isclicked)
btn3.pack(side='left',expand='true',fill='both')

btn4=Button(btnrow3,text="-",font=('algerian',25),relief=GROOVE,border=0,command=btn_diif_isclicked)
btn4.pack(side='left',expand='true',fill='both')




btn1=Button(btnrow4,text="1",font=('algerian',20),relief=GROOVE,border=0,command=btn_1_isclicked)
btn1.pack(side='left',expand='true',fill='both')

btn2=Button(btnrow4,text="2",font=('algerian',20),relief=GROOVE,border=0,command=btn_2_isclicked)
btn2.pack(side='left',expand='true',fill='both')

btn3=Button(btnrow4,text="3",font=('algerian',20),relief=GROOVE,border=0,command=btn_3_isclicked)
btn3.pack(side='left',expand='true',fill='both')

btn4=Button(btnrow4,text="%",font=('algerian',25),relief=GROOVE,border=0,command=btn_percn_isclicked)
btn4.pack(side='left',expand='true',fill='both')




btn1=Button(btnrow5,text=".",font=('algerian',20),relief=GROOVE,border=0,command=btn_dot_isclicked)
btn1.pack(side='left',expand='true',fill='both')

btn2=Button(btnrow5,text="0",font=('algerian',20),relief=GROOVE,border=0,command=btn_0_isclicked)
btn2.pack(side='left',expand='true',fill='both')

btn3=Button(btnrow5,text="=",font=('algerian',25),relief=GROOVE,border=0,command=ruselt)
btn3.pack(side='left',expand='true',fill='both')



win.mainloop()
