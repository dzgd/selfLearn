
from flask import Flask
from flask import request
import os
app = Flask(__name__)
@app.route("/")
def show():
    f = open("pop2.html","rb")
    data = f.read()
    f.close()
    return  data

if __name__ =="__main__":
    app.run()