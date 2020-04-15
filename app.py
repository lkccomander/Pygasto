
from flask import Flask
from WashingMachine import WashingMachine
from Pygasto import *
import requests
import os
import random
import string
import json


# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.
# D:\Repos\Python\HelloPython\names.json

miLavadora = WashingMachine("Samsung","XT5600","SNHT34",100)

miLavadora.DisplayData()

chars = string.ascii_letters +string.digits + '!@#$%^&^*()'
random.seed = (os.urandom(1024))

url = 'https://www.sucursalelectronica.com/redir/redirect.go?country=CR'

names = json.loads(open('names.json').read())

#for name in names:
for x in range (8):
    for name in names:
        name_extra = ''.join(random.choice(string.digits))

    email = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))
    emails = email+' '+password
    print(emails)
    requests.post(url, allow_redirects=False, data={
        'product': email,
        'pass': password
        })
    


@app.route('/')
@app.route('/hello')
@app.route('/hierachy')


def hello():
    # Render the page
    hie = "<br><b>Geography > Region > Availability Zone > Availability Set > Fault Domain ./ Update domain</b><br>"
    return hie
    #return emails

def hierachy():
    
    hie = "Geography > Region > Availability Zone > Availability Set > Fault Domain ./ Update domain"
    return hie

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)


# https://www.sucursalelectronica.com/redir/redirect.go?country=CR
#product: email
#pass: moco34
