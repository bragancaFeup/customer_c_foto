"""
@author: António Brito / Carlos Bragança
(2024)
#objective: app.py

"""""

'''
no PC deve ter o ficheiro datafile.py com

filename = 'data/'

'''

from flask import Flask, render_template, request, session
from datafile import filename
import os

from classes.customer import Customer


from classes.userlogin import Userlogin



app = Flask(__name__)

Customer.read(filename + 'person_foto.db')

Userlogin.read(filename + 'person_foto.db')

prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'fotos')
 
app.config['UPLOAD'] = upload_folder

import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_customerFoto as customerfsub


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
     return gfsub.gform(cname)

    
@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    print(cname)
    return gfTsub.gformT(cname)

@app.route("/customer_foto", methods=["post","get"])
def gformFoto():
    cname = 'Customer'
    return customerfsub.customerFotoform(app,cname)





if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,port=7000)