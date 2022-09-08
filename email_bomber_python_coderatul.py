print(
"""
███████╗███╗   ███╗ █████╗ ██╗██╗     ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║     ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
            version 1.1 : uses app passowrd now, before it used less secure apps
                               Author : linktr.ee/coderatul
                        Before using please read "prerequisite section"
"""
)
from cgitb import text
from email import message
from typing import Text
from getpass4 import getpass
sender = input("Enetr Sender's Gmail Id -> ")
app_password = getpass("Enter App password -> ")
receiver = input("Enter Receiver's Gmail Id -> ")
message = input("Enter Your Message ->")
count = int(input("Enter number of mail's to be sent -> "))
import smtplib 
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(user= sender,password= app_password)
except:
    print("")
    print("""check for the following:
    1. Read prerequisite section 
    2. Check app password
    3. try again and enter details carefully
    """)
else:
    for i in range(count):
        server.sendmail(from_addr= sender,to_addrs= receiver,msg= message)
    if count < 2:
        print(count,"mail have been sent to :",receiver)
    else:
        print(count,"mails have been sent to :",receiver)
    server.close()




