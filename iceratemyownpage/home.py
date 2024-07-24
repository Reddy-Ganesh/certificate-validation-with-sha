from tkinter import *
from tkinter import messagebox
import ast
from PIL import ImageTk,Image



window7 =Tk()


window7.title("home")
window7.configure(bg='black')
window7.resizable(False,False)
window7.geometry('1266x986')
img=PhotoImage(file='g1.png')

def register():
    window7.destroy()
    import registration
def login():
    window7.destroy()
    import login
Label(window7,image=img,border=0,bg='black',width=550,height=600).place(x=720,y=90)

Label(window7,text='welcome',fg='#57a1f8',bg='black',font=('Microsoft Yahei UI Light',45)).place(x=10,y=10)
Label(window7,text='cerificate validation',fg='white',bg='black',font=('Time New Raman',30)).place(x=310,y=150)

frame1=Frame(window7,width=350,height=325,border=5 ,bg='black')
frame1.place(x=300,y=250)
Button(frame1,width=20,pady=4,text='Register',bg='black',activebackground='#78E847',fg='#57a1f8',border=1,font=('Microsoft Yahei UI Light',20),command=register).place(x=30,y=60)
Button(frame1,width=20,pady=4,text='Login', activebackground='#84F7F1',bg='black',border=1,font=('Microsoft Yahei UI Light',20),cursor='hand2',fg='#57a1f8',command=login).place(x=30,y=150)
window7.mainloop()