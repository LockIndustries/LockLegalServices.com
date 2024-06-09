#!/usr/bin/env python

import json
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
from flask import redirect


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os


# Instatiate flask server
app = Flask(__name__)
CORS(app)

# Instantiate mail service
user = "emailservice.lockindustries@gmail.com"
app_password = ""
host = 'smtp.gmail.com'
port = 465

### Define email ###
message = MIMEMultipart()


@app.route('/', methods=['POST','PUT','GET'])
def testit():
  try:
    # print(type(request))
    # print(request)
    # print(request.get_data())
    content = request.get_data().decode('utf-8')
    print(content)

    to = 'michael.c.locker@gmail.com'
    subject = 'test subject'
    content_txt = content #'mail body content attempt 2'


    ### Define email ###
    message = MIMEMultipart()
    # add From 
    message['From'] = Header(user)
    # add To
    message['To'] = Header(to)     
    # add Subject
    message['Subject'] = Header(subject)
    # add content text
    message.attach(MIMEText(content_txt, 'plain', 'utf-8'))

    ### Send email ###
    server = smtplib.SMTP_SSL(host, port) 
    server.login(user, app_password)
    server.sendmail(user, to, message.as_string()) 
    server.quit() 
    print('Sent email successfully')  
  except Exception as e:
    print(e)
  finally:
    return redirect("https://www.locklegalservices.com/disclaimer.html", code=302)

# Run Code
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", ssl_context='adhoc')
    # app.run()
    #app.run(ssl_context='adhoc')
