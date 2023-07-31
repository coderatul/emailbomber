FROM python:3.10.12-alpine
RUN apk update
WORKDIR /emailbomber
COPY emailbomber.py emailbomber.py
COPY ./Welcome/welcome.txt ./Welcome/welcome.txt
CMD "python" "emailbomber.py"
