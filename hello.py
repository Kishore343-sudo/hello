# app.py
from flask import Flask

#Welcome 
app = Flask(_name_)

@app.route('/')
def welcome():
    return 'Welcome to my web application!'

if _name_ == '_main_':
    app.run(host="127.0.0.1",port=8080,debug=True)
