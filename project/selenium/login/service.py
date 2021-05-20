import flask
app=flask.Flask(__name__)
@app.route("/",methods=["GET","POST"])
def login():
     user=flask.request.values.get("user") if "user" in flask.request.values else ""
     pwd=flask.request.values.get("pwd") if "pwd" in flask.request.values else ""
     if user=="xxx" and pwd=="123":
        return flask.redirect("/show")
     else:
        return flask.render_template("login01.html")
@app.route("/show",methods=["GET","POST"])
def show():
    s = "<table border='1'>"
    s = s + "<tr><td>品牌</td><td>型号</td><td>价格</td></tr>"
    s = s + "<tr><td>华为</td><td>P9</td><td>3800</td></tr>"
    s = s + "<tr><td>华为</td><td>P10</td><td>4200</td></tr>"
    s = s + "<tr><td>苹果</td><td>iPhone6</td><td>5800</td></tr>"
    s = s + "</table><p>"
    s = s + "<a href='/'>退出</a>"
    return s
app.run()