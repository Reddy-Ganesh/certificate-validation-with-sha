from tkinter import *
from tkinter import messagebox
import ast


window2 =Tk()
window2.title("login")
window2.configure(bg='#fff')
window2.resizable(False,False)
window2.geometry('1266x986')
img=PhotoImage(file='login.png')



def signup():
    window2.destroy()
    import registration

def login():
    flage=0
    username=user1.get()
    password=pass1.get()
    file=open("datasheet.txt")
    for i in file:
        arr=i.split('#')
        if arr[0]==username and arr[1]==password and arr[2]=='student\n':
            window2.destroy()

            import  studentpage
            flage=1
            break
        elif arr[0]==username and arr[1]==password and arr[2]=='institute':
            window2.destroy()
            import  institutepage
            flage=1
            break
        elif arr[0]==username and arr[1]==password and arr[2]=='student':
            window2.destroy()
            import  studentpage
            
            flage=1
            break
        elif arr[0]==username and arr[1]==password and arr[2]=='institute\n':
            window2.destroy()
            import  institutepage
            flage=1
            break
    if flage==0:
        messagebox.showinfo("invalid","username and passwoard")
def forgetpassword():
    username=user1.get()
    if len(username)==0:
        messagebox.showwarning('username',"enteruser name")
    else:

        window2.destroy()
        import forgetpassword




Label(window2,image=img,border=0,bg='white').place(x=50,y=90)
frame1=Frame(window2,width=350,height=450,bg='#fff')
frame1.place(x=480,y=50)
heading=Label(frame1,text='Sign In',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
def on_enter(e):
    user1.delete(0,'end')
def on_leave(e):
    if user1.get()=='':
        user1.insert(0,"username")

user1 =Entry(frame1,width=25,fg='black', border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
user1.place(x=30,y=80)
user1.insert(0,'username')
user1.bind("<FocusIn>",on_enter)
user1.bind("<FocusOut>",on_leave)
Frame(frame1,width=295,height=2,bg='black').place(x=25,y=107)
def on_enter(e):
    pass1.delete(0,'end')
def on_leave(e):
    if pass1.get()=='':
        pass1.insert(0,"passwaord")

pass1 =Entry(frame1,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))

pass1.place(x=30,y=150)
pass1.insert(0,'password')
pass1.bind("<FocusIn>",on_enter)
pass1.bind("<FocusOut>",on_leave)


Frame(frame1,width=295,height=2,bg='black').place(x=25,y=177)
Button(frame1,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=login).place(x=30,y=220)
Button(frame1,width=39,pady=7,text='forgetpasswaord',bg='white',fg='orange',border=0,command=forgetpassword).place(x=25,y=265)
label=Label(frame1,text='I do not have an acccount',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=300)

signin=Button(frame1,width=6,text='Signup',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
signin.place(x=250,y=300)
window2.mainloop()
