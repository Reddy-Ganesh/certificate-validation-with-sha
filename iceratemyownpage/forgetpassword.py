from tkinter import *
from tkinter import messagebox
import ast



window3 =Tk()
window3.title("logi")
window3.configure(bg='#fff')
window3.resizable(False,False)
window3.geometry('1266x986')
img=PhotoImage(file='login.png')
flage=0



def reset():
    username=user1.get()
    pass2=pass1.get()
    file=open("datasheet.txt","r")
    for i in file:
        arr=i.split('#')
        if arr[0]==username:
            file=open('datasheet.txt','a')
            s=arr[0]
            s1=arr[2]
            pp=str(s)+'#'+str(pass2)+'#'+str(s1)
            file.write("\n")
            file.write(pp)
            
            file.close()
            flage=1
            break
    
    if flage==1:
        window3.destroy()
        import login




Label(window3,image=img,border=0,bg='white').place(x=50,y=90)
frame3=Frame(window3,width=350,height=450,bg='#fff')
frame3.place(x=480,y=50)
heading=Label(frame3,text='Reset',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)
def on_enter(e):
    user1.delete(0,'end')
def on_leave(e):
    if user1.get()=='':
        user1.insert(0,"username")

user1 =Entry(frame3,width=25,fg='black', border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
user1.place(x=30,y=80)
user1.insert(0,'username')
user1.bind("<FocusIn>",on_enter)
user1.bind("<FocusOut>",on_leave)
Frame(frame3,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    pass1.delete(0,'end')
def on_leave(e):
    if pass1.get()=='':
        pass1.insert(0,"passwaord")

pass1 =Entry(frame3,width=25,fg='black',border= 0,bg='white',font=('Microsoft Yahei UI Light',11))
pass1.place(x=30,y=150)
pass1.insert(0,'resetpassword')
pass1.bind("<FocusIn>",on_enter)
pass1.bind("<FocusOut>",on_leave)

###-----------------------------------reset--------------------

Frame(frame3,width=295,height=2,bg='black').place(x=25,y=177)
d=Button(frame3,width=30,pady=5,text='Reset',bg='#57a1f8',fg='white',border=0,command=reset)

d.place(x=30,y=200)


window3.mainloop()