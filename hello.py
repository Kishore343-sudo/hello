# app.py
from flask import Flask

#Welcome 
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my web application!'

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
