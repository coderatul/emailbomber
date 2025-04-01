# 📧 Email-Bomber v2.0.0
![Email Bomber Screenshot v2.0.0](https://i.imgur.com/zSeyXbw.png)
- An open Source free to use email-bomber using python's built-in library SMTP.
- This project's image is also available at dockerhub `docker pull coderatul/emailbomber`
  - use following commands to use it on docker 🐋
  - ```
     docker run --rm -i -t emailbomber /bin/sh
    ```
  - ```
    python3 emailbomber.py
    ```
## GUI version 💻
> checkout [GUI](https://github.com/coderatul/emailGUI.git) version of emailbomber

![gui_emailbomber](https://github.com/user-attachments/assets/f9406245-cf9c-4b82-b525-60be1ba9079f)

## ⚠️ Prerequisite
![Enabling 2-Step Verification Screenshot](https://i.imgur.com/1tUNrsu.png)

### Enabling 2-Step Verification
- Go to your [Google Account](https://myaccount.google.com/) which you would like to send email-bombs from.
- Select [Security](https://myaccount.google.com/security).
- Enable [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification).

### Create App Password
![Create App Password Screenshot](https://i.imgur.com/KdU5Erp.png)
- Go to [App Passwords](https://myaccount.google.com/apppasswords).
- Select app as Mail.
- Select device as your device e.g. Windows Computer etc.
  - If you do not have this option available:
    - You turned on Advanced Protection.
    - 2-Step Verification is not set up for your account.
    - 2-Step Verification is only set up for security keys.
    - Your account is under the control by work, school, or an organization.

### Use App Password
![App Password](https://i.imgur.com/krkn5EX.png)
- Copy App Password.
- Use App Password in Email-Bomber script (you can input it safely into the prompt without it displaying to the console).

### Setup App Password in Email-Bomber script
![Folder Structure](./resources/images/folder-structure.jpg)
- Create User_Credentials folder in Email-Bomber folder 
- Replicate the folder structure
- Paste App Password in app_password.txt
- Paste sender's email in sender.txt 
- You're good to go!!

## 📑 Installation Guide
### Termux
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
### Linux Distributions
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

## 📇 License
```
MIT License

Copyright (c) 2022-Present, Atul Kushwaha.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🤵 Authors
- [@coderatul](https://github.com/coderatul)

## ❔ Questions/Feedback
If you have any questions or feedback, please reach out in [issues](https://github.com/coderatul/emailbomber/issues).
