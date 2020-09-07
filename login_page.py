from tkinter import *
from tkinter import messagebox
import re
import os

import sqlite3
conn = sqlite3.connect('signindb.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Users (Full_Name TEXT, Email TEXT primary key, Password Text, Phone Text)''')
cur.close()
conn.commit()
conn.close()


window = Tk()
window.title("Welcome to registration page")
window.geometry("500x500")

def clearallfieds():
    v_mail.set("")
    v_cpswd.set("")
    v_pswd.set("")
    v_ph.set("")
    v_fname.set("")

def callloginpage():
    window.destroy()
    os.system("python login.py")

v_fname = StringVar()
v_pswd = StringVar()
v_cpswd = StringVar()
v_gndr = IntVar()
v_ph = StringVar()
v_mail = StringVar()
v_country = StringVar()

def phone_validation(v_ph):
    if v_ph.isdigit():
        return True
    elif len(v_ph)>10:
        messagebox.showinfo("Information", "Phone no can't be more than 10 digits")
        return False

    else:
        messagebox.showinfo("Information", "Only digits are allowd")
        return False

def email_validation(user_email):
    if re.match("^.+@[a-zA-Z]+[.][a-zA-Z]+", user_email) is not None:
        return True
    else:
        messagebox.showinfo("Information", "Invalid Email")
        return False

def validateAllFields():
    if v_fname.get() =="":
        messagebox.showinfo("Information", "please enter full name to proceed")
    elif v_pswd.get() =="":
        messagebox.showinfo("Information", "please enter Password to proceed")
    elif v_cpswd.get() =="":
        messagebox.showinfo("Information", "please conform Password to proceed")
    elif v_ph.get() == "":
        messagebox.showinfo("Information", "please enter phone number to proceed")
    elif len(v_ph.get())!=10:
        messagebox.showinfo("Information", "please enter a valid 10 digit phone number to proceed")
    elif v_mail.get() =="":
        messagebox.showinfo("Information", "please enter your E-mail to proceed")
    elif v_gndr.get() == "":
        messagebox.showinfo("Information", "please Select your gender to proceed")

    elif v_country.get() =="" or v_country.get() =="Select your Country":
        messagebox.showinfo("Information", "please Select your country to proceed")
    elif v_pswd.get() != v_cpswd.get():
        messagebox.showinfo("Information", "Password mismatch")
    elif v_mail.get() !="":
        status= email_validation(v_mail.get())
        if (status):
            conn = sqlite3.connect('signindb.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO Users (Full_Name , Email , Password, Phone ) 
                                                VALUES ("%s","%s","%s","%s")''' %(v_fname.get(), v_mail.get(), v_pswd.get(), v_ph.get() ))
            cur.close()
            conn.commit()
            conn.close()

            messagebox.showinfo("Information", "Registration Successful")
    else:

        messagebox.showinfo("Information", "Registration Successful")




Heading = Label(window, text="New Users Register Here",font=("bold",17))
Heading.place(x= 100, y=30)
name = Label(window, text="Full Name                     :", font=("bold",12))
name.place(x= 80, y=90)
name_v = Entry(window, textvariable=v_fname,width=18)
name_v.place(x= 250, y=90)

password = Label(window, text="Password                     :", font=("bold",12))
password.place(x= 80, y=120)
password_v = Entry(window, show = "*", textvariable=v_pswd, width=18)
password_v.place(x= 250, y=120)

cpassword = Label(window, text="Conform Password     :", font=("bold",12))
cpassword.place(x= 80, y=150)
cpassword_v = Entry(window, show = "*", textvariable=v_cpswd, width=18)
cpassword_v.place(x= 250, y=150)

phone = Label(window, text="Phone                           :", font=("bold",12))
phone.place(x= 80, y=180)
phone_v = Entry(window, textvariable=v_ph, width=18)
phone_v.place(x= 250, y=180)

valid_ph = window.register(phone_validation)
phone_v.config(validate="key", validatecommand=(valid_ph, "%P"))

mail = Label(window, text="Email                            :", font=("bold",12))
mail.place(x= 80, y=210)
mail_v = Entry(window, textvariable=v_mail,width=18)
mail_v.place(x= 250, y=210)



gender = Label(window, text="Gender                         :", font=("bold",12))
gender.place(x= 80, y=240)
Radiobutton(window, text="Male", fg= "blue", bg= "light blue", padx=5, textvariable=v_gndr, value=1).place(x= 250, y=240)
Radiobutton(window, text="Female", fg= "Red",bg= "light blue", padx=20, textvariable=v_gndr, value=2).place(x= 320, y=240)

cntr = Label(window, text="Country                         :", font=("bold",12))
cntr.place(x= 80, y=280)

list_contry = ["India", "Australia", "Japan", "USA", "England"]
droplist = OptionMenu(window, v_country, *list_contry)
droplist.config(width=18, bg="green")
v_country.set("Select your Country")
droplist.place(x=250, y=280)

skill = Label(window, text="Skills                         :", font=("bold",12))
skill.place(x= 80, y=320)

skill1 = Checkbutton(window, text="python", bg="light blue").place(x=250, y=320)
skill2 = Checkbutton(window, text="java", bg="light blue").place(x=335, y=320)
skill3 = Checkbutton(window, text="php", bg="light blue").place(x=410, y=320)

but1 = Button(window, text="REGISTER", command=validateAllFields, bg="light green", font=("bold",12))
but1.place(x= 360, y=390)
but2 = Button(window, text="CLEAR", command=clearallfieds, bg="Blue", font=("bold",12))
but2.place(x= 250, y=390)
but3 = Button(window, text="EXISTING USER ?", command=callloginpage, bg="Blue", font=("bold",12))
but3.place(x= 80, y=390)



#messagebox.showinfo("Information", "Only digits are allowd")
window.mainloop()