from flask import Flask,make_response,request,session

app = Flask(__name__) 
app.secret_key = "Rahul"

@app.route('/')
def home():
    return "Home page"

@app.route('/setData')
def fun():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return "Hello all"

@app.route('/getData')
def getData():
    if 'name' in session.keys():
        name = session['name']
        print(name)
        return name
    else:
        return "No data"
    
app.route('/clearSession')
def clearSession():
    session.clear()

if __name__=="__main__":
    app.run(port=3000,debug=True)