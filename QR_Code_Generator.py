import pandas as pd
import pyqrcode as pqr
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
def createQR():
    df=pd.read_csv("citizen.csv")
    #print(df.head())
    for index,values in df.iterrows():
        Id=values["UniqueId"]
        name=values["Name"]
        dob=values["DOB"]
        address=values["Address"]
        #gen=values["Gender"]
        #stay=values["Stay"]
        #mob=values["Mobile"]
        
        data=f'''
        ID: {Id} \n
        Name: {name} \n
        Date_Of_Birth: {dob} \n
        Address: {address}\n
        '''
       # print(data)
        fname=f"{Id}.svg"
        image=pqr.create(data)
        image.svg(fname,scale=1)
        #sendemail(email,fname)
createQR()