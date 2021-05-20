import flask
import os
app=flask.Flask(__name__)
def getfile(filename):
    data=b""
    if os.path.exists(filename):
        fobj=open(filename,"rb")
        data=fobj.read()
        fobj.close()
    return data
@app.route("/")
def index():
    return getfile("books.html")
@app.route("/<section>")           #注意</section>有尖括号
def process(section):
    data=""
    if section!="":
        data=getfile(section)
    return data
if __name__=="__main__":
    app.run()

