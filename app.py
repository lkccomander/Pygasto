
from flask import Flask
from WashingMachine import WashingMachine
from Pygasto import *
from datetime import date
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

#Mis Gastos

#    def __init__(self, p_gastodesc, p_gastocomercio, p_gastodate, p_gastomonto,p_gastomisc,p_gastomisc2):

today = date.today()
d1 = today.strftime("%d/%m/%Y")

migasto = Pygasto("Alimento Para Perro","Mall Pet",d1,5000,"NA","NA")

miLavadora = WashingMachine("Samsung","XT5600","SNHT34",100)

print('-----------------------------------------------------')

print(migasto.DisplayStr())

miLavadora.DisplayData()

chars = string.ascii_letters +string.digits + '!@#$%^&^*()'
random.seed = (os.urandom(1024))

url = 'https://www.sucursalelectronica.com/redir/redirect.go?country=CR'

names = json.loads(open('names.json').read())

#for name in names:


print('-----------------------------------------------------')
for x in range (2):
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
    
print('-----------------------------------------------------')

@app.route('/')
@app.route('/hello')
@app.route('/hierachy')


def hello():
    # Render the page
    hie1 = '<hr width="500px;" color="red" size="10">'
    hie2 =  "Test: <br>" + str(migasto.DisplayStr())
    hi3 = '<br>'
    hie =  "<br><b>Geography > Region > Availability Zone > Availability Set > Fault Domain ./ Update domain</b><br>"
    
   
    return hie1+hie + hie1 +hie2 +hie1
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
