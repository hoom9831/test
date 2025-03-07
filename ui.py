from tkinter import *
from tkinter import messagebox
import db_

win = Tk()
win.geometry('800x550+250+100')
win.config(bg='#281264')
db=db_.functions('someone.db')


#_________________________________________________________________________________________


def insert(): 
    fname=ent_fname.get()
    lname=ent_lname.get()
    term=ent_term.get()
    password=ent_password.get()
    db.insert_(fname,lname,term,password)
    show__()
    clear_()

def clear_():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_term.delete(0,END)
    ent_password.delete(0,END)

def exit_():
    ask=messagebox.askquestion("exit",'do you want to go?')
    if  ask == 'yes':
        win.destroy()

def show__():
    lst.delete(0,END)
    y=db.show_()
    for i in y:
        z=list(i)
        lst.insert(END,f'{z[0]} {z[1]} {z[2]} {z[3]} ')


def delete__():

    index=lst.curselection()      
    if index:                     
        record=lst.get(index)     
        x=(str(record).split(" "))

    fname=ent_fname.get()
    lname=ent_lname.get()
    term=ent_term.get()
    password=ent_password.get()
    id=x[0]
    db.delet_(id,fname,lname,term,password)
    show__()
    clear_()

def serch_(event):
    lst.delete(0,END)
    password=ent_serch.get()
    z=list(db.serch(password))
    for i in z:
        lst.insert(END,f'{i[0]} {i[2]} {i[3]}')


#_________________________________________________________________________________________



btn_show=Button(win,text='مشاهده همه',font='raleway 18',width='8',height='1',bg='#0000ff',command=show__)
btn_show.place(x='550',y='170')
'____________________________________________________________'
btn_insert=Button(win,text='اضافه کردن',font='raleway 18',width='8',height='1',bg='#00ff00',command=insert)
btn_insert.place(x='550',y='220')
'____________________________________________________________'
btn_clear=Button(win,text='پاک کردن',font='raleway 18',width='8',height='1',bg='#ffff00',command=clear_)
btn_clear.place(x='550',y='270')
'____________________________________________________________'
btn_delete=Button(win,text='حذف کردن',font='raleway 18',width='8',height='1',bg='orange',command=delete__)
btn_delete.place(x='550',y='320')
'____________________________________________________________'
btn_exit=Button(win,text='بستن',font='raleway 18',width='8',height='1',bg='#ff0000',command=exit_)
btn_exit.place(x='550',y='370')
'____________________________________________________________'



#_________________________________________________________________________________________



lbl_fname=Label(win,text='نام:',font='raleway 18',width='8',height='1',bg='#281264')
lbl_fname.place(x='20',y='30')


lbl_lname=Label(win,text='نام خانوادگی:',font='raleway 18',width='8',height='1',bg='#281264')
lbl_lname.place(x='20',y='100')


lbl_term=Label(win,text='دوره:',font='raleway 18',width='8',height='1',bg='#281264')
lbl_term.place(x='420',y='30')


lbl_password=Label(win,text='رمز ورود:',font='raleway 18',width='8',height='1',bg='#281264')
lbl_password.place(x='420',y='100')


lbl_serch=Label(win,text='جست و جو',font='raleway 18',width='8',height='1',bg='#281264')
lbl_serch.place(x='100',y='500')



#_________________________________________________________________________________________



ent_fname=Entry(win,font='raleway 18',width='15')
ent_fname.place(x='170',y='30')


ent_lname=Entry(win,font='raleway 18',width='15')
ent_lname.place(x='170',y='100')


ent_term=Entry(win,font='raleway 18',width='15')
ent_term.place(x='570',y='30')


ent_password=Entry(win,font='raleway 18',width='15')
ent_password.place(x='570',y='100')


ent_serch=Entry(win,font='raleway 18',width='15')
ent_serch.place(x='210',y='500')



#_________________________________________________________________________________________

lst=Listbox(win,font='raleway 18',width='40',height='10')
lst.place(x='20',y='150')

#_________________________________________________________________________________________
#197d5d

win.bind('<Return>',serch_)
win.mainloop()