from flask import Flask, render_template, request
from calendar import isleap
import smtplib
from email.message import EmailMessage
from os import environ
from string import Template

app = Flask(__name__)
password = environ.get('slaptazodis')

def funkcija(emailas, subject, zinute):
        
    email = EmailMessage()
    email['from'] = 'Python'
    email['to'] = emailas
    email['subject'] = subject
    email.set_content(zinute)


    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('bandymas147852@gmail.com', password)
        smtp.send_message(email)


@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        email = request.form['email']
        subj = request.form['subject']
        zin = request.form['zinute']     
        funkcija(email, subj, zin)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


