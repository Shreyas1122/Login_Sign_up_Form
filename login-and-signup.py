#login/signup screen
import mysql.connector
from tkinter import *
con=mysql.connector.connect(host='localhost',password='shreyas@29',user='root')
cur=con.cursor(buffered=True)
try:
    cur.execute("use login_signup;")
    con.commit()
except:
    cur.execute("create database login_signup;")
    con.commit()

try:
    cur.execute("describe login_table;")
    con.commit()
except:
    cur.execute("create table login_table(username varchar(20),password  varchar(20),con_password varchar(20));")
    con.commit()

def successfulpage():
    if(len(se1.get())==0 or len(se2.get())==0 or len(se3.get())==0):
        l=Label(f33,text="All the Entries should be Filled",fg="red")
        l.pack(side="top")
    else:
        global lulla
        if(se2.get()==se3.get()):
            cur.execute(f"insert into login_table(username,password,con_password) values('{se1.get()}','{se2.get()}','{se3.get()}');")
            con.commit()
            newscreen("signupsuccessful_screen")
            try:
                lulla.destroy()
            except:
                lulla=Label()
             
        else:
            lulla=Label(f33,text="please enter the password that matches previous one",fg="red")
            lulla.pack(side="top")
       


def signup():
    global signup_window
    signup_window=Toplevel()
    signup_window.title("Signup")
    signup_window.config(bg="white")
    signup_window.geometry('800x700')
    signup_window.maxsize(800,700)
    signup_window.minsize(800,700)
    global f11
    f11=Frame(signup_window)
    f11.pack(side="top")
    sl0=Label(f11,text="SIGN IN",font="TimesNewRoman  40 bold").pack(side="top",pady=45,)
    global sl1
    sl1=Label(f11,text="Enter your username*",font="TimesNewRoman 22 bold")
    sl1.pack(side="top")
    global se1
    se1=Entry(f11,width=30,font="TimesNewRoman 18 ",relief="solid",)
    se1.pack(side="top")
    se1.bind('<FocusIn>',focusin2)
    se1.bind('<FocusOut>',focusout2)
    global f22
    f22=Frame(signup_window)
    f22.pack(side="top",pady=50)
    global sl2
    sl2=Label(f22,text="Enter your  password*",font="TimesNewRoman 22 bold")
    sl2.pack(side="top")
    global se2
    se2=Entry(f22,width=30,font="TimesNewRoman 18 ",relief="solid")
    se2.pack(side="top")
    se2.bind('<FocusIn>',focusin3)
    se2.bind('<FocusOut>',focusout3)
    global sl3
    global se3
    global f33
    f33=Frame(signup_window)
    f33.pack(side="top")
    sl3=Label(f33,text="Confirm the password*",font="TimesNewRoman 22 bold",)
    sl3.pack(side="top",pady=10)
    se3=Entry(f33,width=30,font="TimesNewRoman 18",relief="solid")
    se3.pack(side="top")
    se3.bind('<FocusIn>',focusin4)
    se3.bind('<FocusOut>',focusout4)
    global f44
    f44=Frame(signup_window)
    f44.pack(side="top")
    b1=Button(f44,text="Sign Up",command=successfulpage,font="TimesNewRoman 17 bold",bg="yellow")
    b1.pack(side="top")
    signup_window.mainloop()

def newscreen(par):
    global page1
    page1=Toplevel()
    page1.title(par)
    page1.config(bg="white")
    page1.geometry('800x700')
    page1.maxsize(800,700)
    page1.minsize(800,700)
    f1=Frame(page1)
    f1.pack()
    l1=Label(f1,text="login or sign up successfully my dear",font="TimesNewRoman 22 bold").pack(side="top")
    

def loginsuccessful():
    global y
    cur.execute("select username,password from login_table;")
    result=cur.fetchall()
    for i in result:
        for j in range(0,1,1):
            if(i[j]==e1.get() and i[1]==e2.get()):
                newscreen("LoginSuccessfulScreen")
            else:
                try:
                    k=y.winfo_exists()
                    if(k==1):
                        pass
                except:
                    y=Label(hh,text="Please Enter The Correct Username or Password",fg="red")
                    y.pack(side="top")
                
    con.commit()

def update_password():
    cur.execute("select username from login_table;")
    result=cur.fetchall()
    for i in result:
        for j in range(0,1,1):
            if(i[j]==se5.get()):
                cur.execute(f"UPDATE login_table SET password='{se6.get()}',con_password='{se6.get()}' WHERE username='{se5.get()}'")
                con.commit()
                l=Label(f77,text="password changes successfully").pack(side="top")
def update_passwordwindow():
    global pager
    pager=Toplevel()
    pager.title("Update password")
    pager.config(bg="white")
    pager.geometry('800x700')
    pager.maxsize(800,700)
    pager.minsize(800,700)
    f1=Frame(pager)
    f1.pack()
    l=Label(f1,text="Update the password",font="TimesNewRoman 22 bold")
    l.pack(side="top")
    global f55
    f55=Frame(pager)
    f55.pack(side="top",pady=50)
    global sl5
    sl5=Label(f55,text="Enter your username associate with Account*",font="TimesNewRoman 22 bold")
    sl5.pack(side="top")
    global se5
    se5=Entry(f55,width=30,font="TimesNewRoman 18 ",relief="solid")
    se5.pack(side="top")
    se5.bind('<FocusIn>',focusin6)
    se5.bind('<FocusOut>',focusout6)
    global f66
    global sl6
    global se6
    f66=Frame(pager)
    f66.pack(side="top")
    sl6=Label(f66,text="Confirm the password*",font="TimesNewRoman 22 bold",)
    sl6.pack(side="top",pady=10)
    se6=Entry(f66,width=30,font="TimesNewRoman 18",relief="solid")
    se6.pack(side="top")
    se6.bind('<FocusIn>',focusin7)
    se6.bind('<FocusOut>',focusout7)
    global f77
    f77=Frame(pager)
    f77.pack(side="top")
    b=Button(f77,text="confirm",command=update_password).pack(side="top")
    
    
    
def focusin(event):
    e1.config(highlightthickness=3, highlightbackground="red")
    l1.config(fg="red")
    
    
def focusout(event):
    e1.config(highlightthickness=1, highlightbackground="black")
    l1.config(fg="black")
    
    if(len(e1.get())==0):
        global lab
        lab=Label(f1,text="please Enter any username",fg="red")
        lab.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab.destroy()
        except:
            lab=Label()
        
def focusin1(event):
    e2.config(highlightthickness=3, highlightbackground="red")
    l2.config(fg="red")
def focusout1(event):
    e2.config(highlightthickness=1, highlightbackground="black")
    l2.config(fg="black")
    if(len(e2.get())==0):
        global labb
        labb=Label(f,text="please Enter any Password",fg="red")
        labb.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            labb.destroy()
        except:
            labb=Label()
def focusin2(event):
    se1.config(highlightthickness=3, highlightbackground="red")
    sl1.config(fg="red")
def focusout2(event):
    se1.config(highlightthickness=1, highlightbackground="black")
    sl1.config(fg="black")
    if(len(se1.get())==0):
        global lab1
        lab1=Label(f11,text="please Enter any username",fg="red")
        lab1.pack(side="top")
    else:
        try:
            lab1.destroy()
        except:
            lab1=Label()
        
def focusin3(event):
    se2.config(highlightthickness=3, highlightbackground="red")
    sl2.config(fg="red")
def focusout3(event):
    se2.config(highlightthickness=1, highlightbackground="black")
    sl2.config(fg="black")
    if(len(se2.get())==0):
        global lab2
        lab2=Label(f22,text="please Enter a password(Including special characters,uppercase,numbers)",fg="red")
        lab2.pack(side="top")
    else:
        try:
            lab2.destroy()
        except:
            lab2=Label()
        

    
def focusin4(event):
    se3.config(highlightthickness=3, highlightbackground="red")
    sl3.config(fg="red")
def focusout4(event):
    se3.config(highlightthickness=1, highlightbackground="black")
    sl3.config(fg="black")
    if(len(se3.get())==0):
        global lab3
        lab3=Label(f33,text="please Enter to confirm password",fg="red")
        lab3.pack(side="top")
        
    else:
        try:
            lab3.destroy()
        except:
            lab3=Label()
def focusin6(event):
    se5.config(highlightthickness=3, highlightbackground="red")
    sl5.config(fg="red")
def focusin7(event):
    se6.config(highlightthickness=3, highlightbackground="red")
    sl6.config(fg="red")
def focusout6(event):
    se5.config(highlightthickness=1, highlightbackground="black")
    sl5.config(fg="black")
    if(len(se5.get())==0):
        global lab355
        lab355=Label(f55,text="please enter your old username correctly",fg="red")
        lab355.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab355.destroy()
        except:
            lab355=Label()
def focusout7(event):
    se6.config(highlightthickness=1, highlightbackground="black")
    sl6.config(fg="black")
    if(len(se6.get())==0):
        global lab333
        lab333=Label(f66,text="please Enter to confirm password",fg="red")
        lab333.pack(side="top")
        print("why entry is empty dear")
    else:
        try:
            lab333.destroy()
        except:
            lab333=Label()





    
    
root=Tk()
f1=Frame(root)
root.geometry('800x600')
root.maxsize(800,600)
root.minsize(800,600)
f1.pack(side="top")
l0=Label(f1,text="LOGIN",font="TimesNewRoman  40 bold").pack(side="top",pady=45,)
l1=Label(f1,text="Enter your username*",font="TimesNewRoman 22 bold")
l1.pack(side="top")
e1=Entry(f1,width=30,font="TimesNewRoman 18 ",relief="solid",)
e1.pack(side="top")
e1.bind('<FocusIn>',focusin)
e1.bind('<FocusOut>',focusout)
f2=Frame(root)
f2.pack(side="top",pady=50)
f=Frame(f2)
l2=Label(f2,text="Enter your password*",font="TimesNewRoman 22 bold")
l2.pack(side="top")
e2=Entry(f2,width=30,font="TimesNewRoman 18 ",relief="solid")
e2.pack(side="top")
e2.bind('<FocusIn>',focusin1)
e2.bind('<FocusOut>',focusout1)
f.pack(side="top")
v=Button(f2,text="Forgot my password ?",command=update_passwordwindow)
v.pack(side="top",pady=10)
Label(f2,text="New here ?",font="TimesNewRoman 15 bold",fg="blue").pack(side="left",padx=65,pady=20)
bu=Button(f2,text="Sign In",command=signup,bg="blue",fg="white")
bu.pack(side="left")
hh=Frame(root)
hh.pack(side="top")
f3=Frame(root)
f3.pack(side="top")
b1=Button(f3,text="Login",command=loginsuccessful,font="TimesNewRoman 17 bold",bg="yellow")
b1.pack(side="top")






root.mainloop()
