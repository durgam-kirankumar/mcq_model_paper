import os
import tkinter.messagebox 
os.system('cls')
# ==========================
import tkinter
from tkinter import messagebox
from pathlib import Path
text = open('C:\\Users\\Durgam Sai Kumar\\Desktop\\python_2000\\test_data.txt')
temp_path = Path('C:\\Users\\Durgam Sai Kumar\\Desktop\\python_2000\\temp_data.txt')
question_option = []
for x in text:
    if x[-1] == '\n':
        x = x[:-1]
    x = x.split(', ')
    print(x)
    question_option.append(x)
text.close()
# text = text.split('|')



home_window = tkinter.Tk()
home_window.minsize(600,450)
home_window.maxsize(600,450)
home_window.title('online_test')
color = "#a5faa8"
index_number = 0
user_option = tkinter.IntVar()
# print(user_option.get())
user_chosen = {}
if temp_path.exists():
    tmp = open(temp_path,'r')
    for f in tmp:
        if x[-1] == '\n':
            f = f[:-1]
        f = f.split(', ')
        user_chosen[f[0]] = [f[1], f[2]]
    tmp.close()
        
        
is_submit = 0




home_window.config(bg=color)
test_name = tkinter.Label(home_window,text='Test',font=('bold',17),bg=color)
test_name.place(x=260,y=10)

def user_select():
    temp = open(temp_path,'a')

    result = 'wrong'
    if question_option[index_number][user_option.get()] == question_option[index_number][4]:
        result = 'correct'
        
    user_chosen[question_option[index_number][0]] = [user_option.get(),result]
    temp.write(f'{question_option[index_number][0]}, {user_option.get()}, {result}\n')
    temp.close()
    os.system('cls')
    print(user_chosen)
    if len(question_option) == len(user_chosen):
        next_button.place(x=300,y=300)
        submit_button.place(x=450,y=300)
    
   

question_1 = tkinter.Label (home_window,text=f'{index_number +1}. {question_option[index_number][0]}',font=('bold',17), bg=color)
question_1.place(x=120,y=60)
opt_1 = tkinter.Radiobutton(home_window, command = user_select, text=question_option[index_number][1],  variable=user_option, value=1 , font=('bold',17), bg=color)
opt_1.place(x=150,y=100)
opt_2 = tkinter.Radiobutton(home_window, command = user_select, text=question_option[index_number][2],  variable=user_option, value=2 , font=('bold',17), bg=color)
opt_2.place(x=150,y=140)
opt_3 = tkinter.Radiobutton(home_window, command = user_select, text=question_option[index_number][3],  variable=user_option, value=3 , font=('bold',17), bg=color)
opt_3.place(x=150,y=180)
ans_button = tkinter.Label(home_window,text=f'correct :{question_option[index_number][4]}',font=('bold',15),bg=color,fg='green')

def check_result():
    if user_chosen[question_option[index_number][0]][1] == 'correct':
        question_1.config(fg='green')
        ans_button.place_forget()
    else:
        question_1.config(fg='red')
        ans_button.config(text=f'correct : {question_option[index_number][4]}')
        ans_button.place(x=150,y=220)
        
        
    
def next():
    global index_number
    if index_number < len(question_option)-1:
        index_number += 1
    question_1.config(text= f'{index_number+1}. {question_option[index_number][0]}')
    opt_1.config(text = question_option[index_number][1])
    opt_2.config(text = question_option[index_number][2])
    opt_3.config(text = question_option[index_number][3])
    back_button.config(state='normal')
    opt_index = user_chosen.get(question_option[index_number][0],'0')[0]
    user_option.set(opt_index)
    if is_submit:
        check_result()
    if index_number == len(question_option)-1:
        next_button.config(state='disabled')

        
    
    
def back():
    global index_number
    if index_number > 0:
        index_number -= 1
    question_1.config(text=f'{index_number+1}. {question_option[index_number][0]}')
    opt_1.config(text=question_option[index_number][1])
    opt_2.config(text=question_option[index_number][2])
    opt_3.config(text=question_option[index_number][3])
    next_button.config(state='normal')
    opt_index = user_chosen.get(question_option[index_number][0],'0')[0]
    user_option.set(opt_index)
    if is_submit:
        check_result()
    if index_number == 0:
        back_button.config(state='disabled')

def submit():
    marks = 0
    for x in user_chosen.values():
        if x[1] == 'correct':
            marks += 1
    text = (f'Total marks {marks}\{len(question_option)}')
    tkinter.messagebox.showinfo('Result ', text)
    submit_button.config(state='disabled')
    opt_1.config(state='disabled')
    opt_2.config(state='disabled')
    opt_3.config(state='disabled')
    global is_submit
    is_submit = 1
    if is_submit:
        check_result()
    os.remove(temp_path)
    
    
    
        

back_button = tkinter.Button(home_window,command=back,state='disabled',text='Back',font=('bold',15),width=8)
back_button.place(x=30,y=300)

next_button = tkinter.Button(home_window,command = next,text = 'Next',font=('bold',15),width=8)
next_button.place(x=450,y=300)

submit_button = tkinter.Button(home_window,command=submit,text='submit',font=('bold',15),width=8)
# submit_button.place(x=450,y=300)
submit_button.forget()


home_window.mainloop()


