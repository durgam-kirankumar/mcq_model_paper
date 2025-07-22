import os
os.system('cls')
# ==========================
import tkinter
import tkinter.messagebox
from pathlib import Path
students = ['kiran','saikumar','vamshi','harika','sahith']
passwords = ['111','222','333','444','555']


main_window = tkinter.Tk()
main_window.minsize(350,250)
main_window.maxsize(350,250)
main_window.title('Login_page')
color = "#58e9fc"
main_window.config(bg=color)
username = tkinter.StringVar()
password_s = tkinter.StringVar()

user_name = tkinter.Label(main_window,text='Username',font=('bold',17),bg=color)
user_name.place(x=10,y=50)
pass_word = tkinter.Label(main_window,text='password',font=('bold',17),bg=color)
pass_word.place(x=10,y=90)

user_name_box = tkinter.Entry(main_window,font=('bold',15),textvariable=username,width=17)
user_name_box.place(x=130,y=50)
pass_word_box = tkinter.Entry(main_window,show='*',font=('bold',15),textvariable=password_s,width=17)
pass_word_box.place(x=130,y=90)

def validation():
    un = username.get()
    pw = password_s.get()
    
    if un in students and pw == passwords[students.index(un)]:
        x = (f'Hello {un}\n WELCOME')
        tkinter.messagebox.showinfo('WELCOME',x)
    else:
        text = f'wrong username or passwrod'
        x = (un,pw)
    tkinter.messagebox.showerror('Invalid',text)

login_button = tkinter.Button(main_window,command=validation,text='login',font=('bold',14),width=8)
login_button.place(x=160,y=140)
main_window.mainloop()