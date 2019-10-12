from tkinter import *

def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
    
    # create a Form label 
    Label(text="Choose Login", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
 
    # create Login Button 
    Button(text="Traffic Police", height="2", width="30",command=Login).pack() 
    Label(text="").pack() 

    Button(text="Healthcare", height="2", width="30",command=Login).pack() 
    Label(text="").pack()

    Button(text="Banking", height="2", width="30",command=Login).pack() 
    Label(text="").pack()
 
    main_screen.mainloop()
    
def Login():
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

def login_verification():
    print("Working..........")



main_account_screen()
