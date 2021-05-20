'''#####服务端口处于打开，且服务器获取GET发送的数据#########
import flask
app=flask.Flask(__name__)
@app.route("/")
def index():
    try:
        p=flask.request.args.get("province") if "province" in flask.request.args else ""
        c = flask.request.args.get("city") if "city" in flask.request.args else ""
        print(p,c)
        return  p+","+c
    except Exception as err:
        return str(err)
app.run()'''

#####服务端口处于打开，且服务器获取POST发送的数据#########
import flask
app=flask.Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    try:
        p=flask.request.form.get("province") if "province" in flask.request.form else ""
        c = flask.request.form.get("city") if "city" in flask.request.form else ""
        note=flask.request.form.get("note") if "note" in flask.request.form else ""
        print(p,c,note)
        return p+"\n"+c+"\n"+note
    except Exception as err:
        print(err)
app.run()


