from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the flask home page"


@app.route('/about')
def about():
    return "This is about page"

@app.route('/user/<username>')
def greet(username):
    return f"THe username is {username}"

if __name__ == '__main__':
    app.run(debug=True)