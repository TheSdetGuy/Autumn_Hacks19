from tkinter import *
import pandas as pd
import numpy as np
import os
import cv2
import numpy as np
import pyzbar.pyzbar as pz

#global k

def Login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="EMAIL ID").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_check).pack()

    
def validation():
    id_log = StringVar()
    qr_window= Toplevel(main_screen)
    qr_window.title("Scanning Window")
    qr_window.geometry("350x350")
    #Label(qr_window, text="Choose one option from the following").pack()
    #Label(qr_window, text="").pack()
    Button(qr_window, text="Scan QR Code", width=15, height=1,command=Qrscan).pack()
    Label(qr_window, text="").pack()
    #Label(qr_window, text="If you are not having QR code scanner then login through ID").pack()
    #Label(qr_window, text="").pack()
    #id_login = Entry(qr_window, textvariable=id_log)
    #id_login.pack()
    #Label(qr_window, text="").pack()
    #Button(qr_window, text="Login through ID", width=15, height=1, command=check).pack()

def check():
    print("hello")

def login_check():
    flag=1
    global k
    df=pd.read_csv("Hack.csv")
    user=str(username_verify.get())
    passw=str(password_verify.get())
    
   # print(user)
   # print(passwo)
    for index,values in df.iterrows():
        email=str(values["Email"])
        password=str(values["Password"])
        depart=str(values["Department"])
        if(email.strip()==user.strip() and password.strip()==passw.strip()):
            
            flag=0
            if(depart=="Police"):
                k=1
                break
            if(depart=="Healthcare"):
                k=2
                break
            if(depart=="Banking"):
                k=3
                break
    
    if(flag==1):
        invalid_user_or_password()
    else:
        validation()
            
def invalid_user_or_password():
    global invalid_screen
    invalid_screen=Toplevel(login_screen)
    invalid_screen.title("Login Failed")
    invalid_screen.geometry("250x200")
    Label(invalid_screen,text="invalid_user_or_password").pack()
    Button(invalid_screen,text="OK",command=delete_not_recognized).pack()

def delete_not_recognized():
    invalid_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("300x250") # set the configuration of GUI window 
    main_screen.title("Account Login") # set the title of GUI window
    
    # create a Form label 
    Label(text="Choose Login", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
 
    # create Login Button 
    Button(text="Police", height="2", width="30",command=Login).pack() 
    Label(text="").pack() 

    Button(text="Healthcare", height="2", width="30",command=Login).pack() 
    Label(text="").pack()

    Button(text="Banking", height="2", width="30",command=Login).pack() 
    Label(text="").pack()
 
    main_screen.mainloop()

def successful():
    global y
    y=str(added_info.get())
    print(y)
    display3_screen = Toplevel(main_screen)
    display3_screen.title("SUCCESFUL")
    display3_screen.geometry("300x250")
    label=Label(display3_screen,text="Data Succesfully submitted",font=("Arial Bold",15),fg="black",bg="yellow")
    label.pack()
    display3_screen.mainloop()

def display2():
    global added_info
    added_info= StringVar()
    display2_screen=Toplevel(main_screen)
    display2_screen.title("ADD INFORMATION")
    display2_screen.geometry("300x250")
    Label(display2_screen,text="Enter the data below").pack()
    added_info_entry = Entry(display2_screen, textvariable=added_info)
    added_info_entry.pack()
    Label(text="").pack()
    Button(display2_screen,text="Submit", height="2", width="10",command=successful).pack() 
    Label(text="").pack()
    display2_screen.mainloop()

def display():
    display_screen = Toplevel(main_screen)
    display_screen.title("DETAILS")
    display_screen.geometry("300x250")
    label=Label(display_screen,text=returndata,font=("Arial Bold",15),fg="black",bg="yellow")
    label.pack()
    Label(text="").pack()
    Button(display_screen,text="Add information", height="4", width="20",command=display2).pack() 
    Label(text="").pack()
    display_screen.mainloop()




def Qrscan():
    global message
    cap=cv2.VideoCapture(0)
    font=cv2.FONT_HERSHEY_PLAIN
    x=0
    while x!=1:
        _,frame = cap.read()
        decodedObjects=pz.decode(frame)
        for obj in decodedObjects:
            Qr=obj.data
            Qr1=Qr.split()
            Qr2=str(Qr1[1])
            returnQr=(Qr2[2:-1])
            #print(k," ",returnQr)
            #exit(0)
            #return 0

            x=1
            cap.release()
            cv2.destroyAllWindows()
            search(returnQr,k)
            #display()
            #print(message)
            #fu()
            return
            
        #cv2.putText(obj.data)
        #cv2.putText(frame,str(obj.data),(50,50),font,3,(255,0,0),3)
        cv2.imshow( "Frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
        
        #retrun 0
        #return False
      # break
    
def search(i,d):
    #banking
    global returndata
    if d is 1:
        dataset = pd.read_csv('Police.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            #dataset.insert(r, "Case Years", "100") 
            #return returndata
            display()
            dataset.loc[c,'Case Years'] = y
        else:
            return "sorry this id does not exist"
    if d is 2:
        dataset = pd.read_csv('Health.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            #return returndata
            display()
            dataset.loc[c,'Disease'] = y
        else:
            return "sorry this id does not exist"
    if d is 3:
        dataset = pd.read_csv('Bank.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            #return returndata
            display()
            dataset.loc[c,'Amount'] = y
        else:
            return "sorry this id does not exist"




main_account_screen()


