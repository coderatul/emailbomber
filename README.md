# Email-Bomber v1.1 📧
- An open Source free to use email-bomber using smtp
- Script Have been updated to google's latest requirements as less secure feature have been disable by Google
- Now we use something known as app password 

![eg](https://user-images.githubusercontent.com/72141859/189071701-9adbfbd6-bfe8-4f79-a7bd-71a7f4005ad5.png)

# Modules Required 📗
- <a href="https://docs.python.org/3/library/smtplib.html"> SMTP</a> is a library used for sending mails in python which stands for simple mail transfer protocol
- <a href="https://pypi.org/project/getpass4/"> getpass4</a> is a library used to hide input text (while inputting password)
```
pip install getpass4
```
#  Prerequisite ⚙️
## Create & use App Passwords

- Go to your Google Account (from which you would send mail).
- Select Security.

- Enable 2FA for your Account.

- Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because :
  -  2-Step Verification is not set up for your account.
  - 2-Step Verification is only set up for security keys.
  - Your account is through work, school, or other organization.
  - You turned on Advanced Protection.

- At the bottom, choose Select app (gmail here) and choose the app you using (gmail here) and then select
  device (windows computer here) and choose the device you’re using(windows computer here) and then Generate.
  
  ![app pass](https://user-images.githubusercontent.com/72141859/189069975-1898d162-e3a9-4cab-b1a0-c95963e65268.png)  
- copy the Appassword and while entering sender's password in the script use this password instead of your gmail accounts password 

  ![app paaas](https://user-images.githubusercontent.com/72141859/189070691-8a5734a7-9272-493a-b9b1-4997d90d8deb.png)


# For Termux
```
pkg install git
```
```
pkg install python
```
```
git clone https://github.com/coderatul/emailbomber
```
```
ls
```
```
cd emailbomber
```
```
python emailbomber.py
```

# For linux distributions
```
sudo apt install git
```
```
sudo apt install python3.8
```
```
sudo apt update && upgrade 
```
```
git clone https://github.com/coderatul/emailbomber
```
```
cd emailbomber
```
```
python emailbomber.py
```
