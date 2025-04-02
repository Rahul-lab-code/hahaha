from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="car">Favorite Car:</label>
        <input type="text" id="car" name="car" required><br>
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    car = request.form.get("car")
    
    return f"<h2>Submitted Data:</h2><p>Name: {name}</p><p>Email: {email}</p><p>Favorite Car: {car}</p>"

if __name__ == '__main__':
    app.run(debug=True)
