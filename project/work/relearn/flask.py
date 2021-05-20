# import flask
# app = flask.Flask(__name__)
# @app.route("/")
# def hello():
#     return "欢迎来到帅帅的世界"
#
# @app.route("/hi")
# def hi():
#     return "欢迎来到美美的世界"
# if __name__ == "__main__":
#     app.run()

# import re
# reg = r"\d+"
# m = re.findall(reg,"ab13df7")
# print(m)

import re
s = "i am testing search function"
reg = r"[A-Za-z]+\b"
m = re.search(reg,s)
while m!=None:
    start = m.start()
    end = m.end()
    print(s[start:end])
    s = s[end:]
    m = re.search(reg,s)
