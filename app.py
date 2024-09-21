from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def register():
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('admin-home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/trends', methods=['GET'])
def trends():
    return render_template('trends.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")