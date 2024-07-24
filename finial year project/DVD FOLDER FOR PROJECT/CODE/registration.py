from tkinter import *
from tkinter import messagebox
import ast

window =Tk()
window.title("signUP")
window.configure(bg='#fff')
window.resizable(False,False)
window.geometry('1266x986')
#----home page---
def home():
    window.destroy()
    import home


#the registration page
def signup():
    username=user.get()
    password=code.get()
    conform=code1.get()
    opt=select_value.get()
    if password==conform:
        try:
            file=open('datasheet.txt','rb')
            d=file.read()
            r=ast.literal_eval(d)
            list1=[username,password,opt]
            r.update(list1)
            file.truncate(0)
            file.close()
            file=open('datasheet.txt','w')
            w=file.write(str(r))
            messagebox.showinfo("show","sucessfully sign up")
        except:
            file=open('datasheet.txt','r')
            
            for i in file:
                s=i.split('#')
                if s[0]==username:
                    messagebox.showwarning("user","username is already exist")
                    break
            else:
                file=open('datasheet.txt','a')
                pp=str(username)+'#'+str(password)+'#'+str(opt)
                file.write("\n")
                file.write(pp)
                flage=True
                file.close()
                window.destroy()
                import login
                
    else:
        messagebox.showerror('invalid'," enter both password and confirm pass")
def  loginpage():
    window.destroy()
    import login


img=PhotoImage(file='login.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(window,width=350,height=450,bg='#fff')
frame.place(x=480,y=50)
heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#####---------------------------------------------------------------------------------
def on_enter(e):#if the mouse is on the text place the it doesnot show the place value
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,"username") #username is the place value of that field

user =Entry(frame,width=25,fg='black', border= 0,bg='white',font=('Microsoft Yahei UI Light',11))#entry is widget used to take the input from the user 
user.place(x=30,y=80) #user is the variable which store the input in it
#place is the widget used to place the field in with position
user.insert(0,'username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#####---------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,"passwaord")

code =Entry(frame,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#####---------------------------------------------------------------------------------
def on_enter(e):#if the mouse is on the text place the it doesnot show the place value
    code1.delete(0,'end')
def on_leave(e):
    if code1.get()=='':
        code1.insert(0,"confirmpassword") #conform password is the place value of that field

code1 =Entry(frame,width=25,fg='black', border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
code1.place(x=30,y=220)
code1.insert(0,'confirmpasswaord')
code1.bind("<FocusIn>",on_enter)
code1.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#####---------------------------------------------------------------------------------
options={1:'student',2:'institute'}
select_value=StringVar()
select_value.set(options[1])
drop1=OptionMenu(frame,select_value,*options.values())

drop1.place(x=30,y=260)

###---------------------------------------------------------------------------------------
Button(frame,width=32,text='Sign up',bg='#57a1f8',fg='black',border=0,command=signup,font=('Microsoft Yahei UI Light',12)).place(x=30,y=300)
label=Label(frame,text='I have an acccount',fg='black',bg='white',font=('Microsoft Yahei UI Light',10))
label.place(x=90,y=350)
signin=Button(frame,width=6,text='login',border=0,bg='white',cursor='hand2',fg='#E15B08',command=loginpage,font=('Microsoft Yahei UI Light',11))
signin.place(x=200,y=350)
Button(frame,width=5,text="home",border=0,bg='black',cursor='hand2',fg='white',command=home,font=('Microsoft Yahei UI Light',11)).place(x=300,y=400)


window.mainloop()