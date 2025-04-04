from flask import Flask,make_response,request

app = Flask(__name__)

@app.route('/')
def home():
    theme = request.cookies.get("theme")
    return theme

@app.route('/cookie')
def setCookie():
    res = make_response("<h1>Cookie is set</h1>")
    res.set_cookie("theme","dark")
    return res

@app.route('/remove')
def removeCookie():
    res = make_response("<h1>Removing the Cookie </h1>")
    res.delete_cookie("theme")
    return res

if __name__=="__main__":
    app.run(port=3000,debug=True)