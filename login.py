from tkinter import *
from tkinter import messagebox
import os
import sqlite3

def fetch():
    conn = sqlite3.connect('signindb.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users WHERE Email=? ', (l_mail.get(),))
    for row in cur.fetchall():
        if row[2] == l_pswd.get():
            window.destroy()
            os.system("python hotel.py")

        else:
            messagebox.showinfo("Information", "Please check your credentials and try again  OR \n Register first, if you are a new user")

    cur.close()
    conn.close()


window = Tk()


def callregpage():
    window.destroy()
    os.system("python login_page.py")

window.title("Welcome to Login page")
window.geometry("500x300")

l_mail = StringVar()
l_pswd = StringVar()

Heading = Label(window, text="Existing Users login Here!",font=("bold",17))
Heading.place(x= 100, y=30)

mail = Label(window, text="Email          :   ", font=("bold",12))
mail.place(x= 130, y=100)
mail_v = Entry(window, textvariable=l_mail,width=18)
mail_v.place(x= 230, y=100)

pswd = Label(window, text="Password    :   ", font=("bold",12))
pswd.place(x= 130, y=130)
pswd_v = Entry(window, show="*", textvariable=l_pswd,width=18)
pswd_v.place(x= 230, y=130)

but1 = Button(window, text="Login", command=fetch, bg="green", width=8, font=("bold",10))
but1.place(x= 250, y=180)
but3 = Button(window, text="New User ?",command=callregpage, bg="light Blue", font=("bold",10))
but3.place(x= 120, y=180)




window.mainloop()
