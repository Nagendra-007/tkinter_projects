from tkinter import *
from tkinter import messagebox
import os
from datetime import date
import time
window = Tk()
f1 = Frame(window, width= 1600, height=170, bg="olivedrab2" )
f1.pack(side=TOP)

f2 = Frame(window, width= 800, height=700, bg="light green" )
f2.pack(side=LEFT)


f3 = Frame(window, width=600, height=700,bg="powder blue" )
f3.pack(side=RIGHT)

f4 = Frame(f3, width=390, height=600,bg="pink" ,highlightbackground="black",bd=10)
f4.place(x=100,y=20)

clock= Label(f1,font=("time",20,"bold"),bg="olivedrab2")
clock.place(x=780,y=140)
def gettime():
    tim=time.strftime("%H:%M:%S")
    clock.config(text=tim)
    clock.after(200,gettime)

gettime()

today = date.today()
dat = today.strftime("%B %d,%Y")
dat1= Label(f1,text=dat,font=("time",20,"bold"),bg="olivedrab2")
dat1.place(x=600,y=140)



rice = IntVar()
dal = IntVar()
Egg_Rice = IntVar()
f_rice = IntVar()
chapati = IntVar()
puri = IntVar()
dosa = IntVar()
upma = IntVar()
c_rice =IntVar()
meals = IntVar()
cbn = IntVar()
extras = IntVar()
mbill = IntVar()
sbill = IntVar()
tbill = IntVar()
txt_input = StringVar()
operator = ""
status = ""
m_price = IntVar()
window.title("welcome to hotel management project")
window.geometry("1400x600")
head = Label(window, text="Hotel Management Project",font=("bold",50),fg="green",bg="olivedrab2")
head.place(x=250, y=15)
Item1 = Label(f2, text="Rice",font=("bold",16),bg="light green")
Item1.place(x=90, y=100)
entr1 = Entry(f2, textvariable=rice,font=("bold",10), width=18)
entr1.place(x=210, y=100)

Item2 = Label(f2, text="Dal",font=("bold",16),bg="light green")
Item2.place(x=90, y=140)
entr2 = Entry(f2, textvariable=dal,font=("bold",10), width=18)
entr2.place(x=210, y=140)

Item9 = Label(f2, text="Meals",font=("bold",16),bg="light green")
Item9.place(x=390, y=140)
entr9 = Entry(f2, textvariable=meals,font=("bold",10), width=18)
entr9.place(x=560, y=140)


Item3 = Label(f2, text="Egg Rice",font=("bold",16),bg="light green")
Item3.place(x=90, y=180)
entr3 = Entry(f2, textvariable=Egg_Rice,font=("bold",10), width=18)
entr3.place(x=210, y=180)

Item10 = Label(f2, text="Chiken Biriyani",font=("bold",16),bg="light green")
Item10.place(x=390, y=180)
entr10= Entry(f2, textvariable=cbn,font=("bold",10), width=18)
entr10.place(x=560, y=180)


Item4 = Label(f2, text="Fried Rice",font=("bold",16),bg="light green")
Item4.place(x=90, y=220)
entr4 = Entry(f2, textvariable=f_rice,font=("bold",10), width=18)
entr4.place(x=210, y=220)

Item11 = Label(f2, text="Extras",font=("bold",16),bg="light green")
Item11.place(x=390, y=220)
entr11= Entry(f2, textvariable=extras,font=("bold",10), width=18)
entr11.place(x=560, y=220)


Item5 = Label(f2, text="Chapati",font=("bold",16),bg="light green")
Item5.place(x=90, y=260)
entr5 = Entry(f2, textvariable=chapati,font=("bold",10), width=18)
entr5.place(x=210, y=260)

Item12 = Label(f2, text="Total Charge",font=("bold",16),bg="light green")
Item12.place(x=390, y=340)
entr12 = Entry(f2, textvariable=tbill,font=("bold",10), width=18)
entr12.place(x=560, y=340)


Item6 = Label(f2, text="Puri",font=("bold",16),bg="light green")
Item6.place(x=90, y=300)
entr6 = Entry(f2, textvariable=puri,font=("bold",10), width=18)
entr6.place(x=210, y=300)

Item13 = Label(f2, text="Mess Charge",font=("bold",16),bg="light green")
Item13.place(x=390, y=260)
entr13 = Entry(f2, textvariable=mbill,font=("bold",10), width=18)
entr13.place(x=560, y=260)


Item7 = Label(f2, text="Dosa",font=("bold",16),bg="light green")
Item7.place(x=90, y=340)
entr7 = Entry(f2, textvariable=dosa,font=("bold",10), width=18)
entr7.place(x=210, y=340)

Item14 = Label(f2, text="Service charge",font=("bold",16),bg="light green")
Item14.place(x=390, y=300)
entr14 = Entry(f2, textvariable=sbill,font=("bold",10), width=18)
entr14.place(x=560, y=300)


Item8 = Label(f2, text="Curd Rice",font=("bold",16),bg="light green")
Item8.place(x=390, y=100)
entr8 = Entry(f2, textvariable=c_rice,font=("bold",10), width=18)
entr8.place(x=560, y=100)
x=" "

def clr():
    rice.set(0)
    dal.set(0)
    Egg_Rice.set(0)
    f_rice.set(0)
    chapati.set(0)
    puri.set(0)
    dosa.set(0)
    upma.set(0)
    c_rice.set(0)
    meals.set(0)
    cbn.set(0)
    extras.set(0)
    mbill.set(0)
    sbill.set(0)
    tbill.set(0)


def tot():
    ricev= rice.get()
    dalv= dal.get()
    Egg_Ricev = Egg_Rice.get()
    f_ricev = f_rice.get()
    chapativ = chapati.get()
    puriv = puri.get()
    dosav = dosa.get()
    upmav = upma.get()
    c_ricev = c_rice.get()
    mealsv = meals.get()
    cbnv = cbn.get()
    extrasv = extras.get()
    mbill.set(int(extrasv)+20*int(ricev) + 10*int(dalv) + 40*int(Egg_Ricev)+40*int(f_ricev)+30*int(chapativ)+30*int(puriv)+25*int(dosav)+25*int(upmav)+20*int(c_ricev)+80*int(mealsv)+120*int(cbnv)
    )
    if mbill.get()==0:
        messagebox.showinfo("Information", "please enter the number of each item purchased")
    else:
        sbill.set(mbill.get() * 0.08)
        tbill.set(mbill.get()+sbill.get())
def log():
    window.destroy()
    os.system("python login.py")


but1 = Button(f2, text="Total",font=("arial",13), width=12,command=tot).place(x=200, y=430)
but2 = Button(f2, text="Clear",font=("bold",13), width=12,command=clr).place(x=370, y=430)
but3 = Button(f2, text="Quit",font=("bold",13), width=12,command=log).place(x=540, y=430)



def onclick(number):
    global operator
    if status == "on":
        operator = operator + str(number)
        txt_input.set(operator)

def onclear():
    global operator
    #operator = operator + str(number)
    if status == "on":
        txt_input.set("")
        operator=""

def onequal():
    #global operator
    #operator = operator + str(number)
    if status == "on":
        txt_input.set(eval(operator))

def back():
    if status == "on":
        global operator
        operator = operator[:-1]
        txt_input.set((operator))

def switchon():
    global status
    if status =="on":
        txt_input.set("")
        onclear()
        status="off"
    else:
        status = "on"
        txt_input.set(0)



txt_disply = Entry(f4,font= ("bold",20),bd=30, insertwidth =4, bg="powder blue", justify="right",textvariable=txt_input)
txt_disply.place(x=6,y=2)
but7 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="7", bg="powder blue",command=lambda: onclick(7)).place(x=2,y=115)
but8 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="8", bg="powder blue",command=lambda: onclick(8) ).place(x=98,y=115)
but9 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="9", bg="powder blue",command=lambda: onclick(9) ).place(x=197,y=115)
buta = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="+", bg="powder blue",command=lambda: onclick("+") ).place(x=293,y=115)
but4 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="4", bg="powder blue",command=lambda: onclick(4)).place(x=2,y=195)
but5 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="5", bg="powder blue",command=lambda: onclick(5) ).place(x=98,y=195)
but6 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="6", bg="powder blue" ,command=lambda: onclick(6)).place(x=197,y=195)
butm = Button(f4, padx=20.5, pady=8, fg="black", font= ("bold",20),text="-", bg="powder blue",command=lambda: onclick("-")).place(x=293,y=195)
but1 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="1", bg="powder blue",command=lambda: onclick(1)).place(x=2,y=275)
but2 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="2", bg="powder blue" ,command=lambda: onclick(2)).place(x=98,y=275)
but3 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="3", bg="powder blue",command=lambda: onclick(3) ).place(x=197,y=275)
butp = Button(f4, padx=19.5, pady=8, fg="black", font= ("bold",20),text="*", bg="powder blue",command=lambda: onclick("*") ).place(x=293,y=275)
but0 = Button(f4, padx=18, pady=8, fg="black", font= ("bold",20),text="0", bg="powder blue",command=lambda: onclick(0) ).place(x=2,y=355)
butC = Button(f4, padx=16, pady=6, fg="black", font= ("bold",20),text="C", bg="powder blue" ,command=lambda: onclear()).place(x=197,y=435)
butd = Button(f4, padx=20.5, pady=8, fg="black", font= ("bold",20),text="/", bg="powder blue",command=lambda: onclick("/") ).place(x=293,y=355)
bute = Button(f4, padx=18, pady=6, fg="black", font= ("bold",20),text="=", bg="powder blue" ,command=lambda: onequal()).place(x=293,y=435)
backspc = Button(f4, padx=8.5, pady=6, fg="black", font= ("bold",20),text="⌫", bg="powder blue" ,command=lambda: back()).place(x=98,y=435)
ltc = Button(f4, padx=20, pady=8, fg="black", font= ("bold",20),text=")", bg="powder blue" ,command=lambda: onclick(")")).place(x=197,y=355)
rtc = Button(f4, padx=20, pady=8, fg="black", font= ("bold",20),text="(", bg="powder blue" ,command=lambda: onclick("(")).place(x=98,y=355)
on = Button(f4, padx=8, pady=1, fg="black", font= ("bold",16),text="ON/\nOFF", bg="powder blue" ,command=lambda: switchon()).place(x=2,y=435)
l2 = Label(f3,text="Mode 2",bg="powder blue",font=(8))
l2.place(x=10,y=10)
l1 = Label(f2,text="Mode 1",bg="light green",font=(8))
l1.place(x=10,y=10)
window.mainloop()