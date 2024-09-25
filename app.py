from flask import Flask, redirect, render_template, request, jsonify
from account import *

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

@app.route('/createAccount', methods=['POST'])
def createAccounts():
     # Retrieve form data sent via AJAX
    data = request.get_json()

    # Access individual form fields (optional)
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    address = data.get('address')
    gender = data.get('gender')
    birthday = data.get('birthday')
    contact = data.get('contact')
    email = data.get('email')
    password = data.get('password')

    # Perform server-side validation or further processing here
    Accounts().create_account(first_name, last_name, address, gender, birthday, contact, email, password)
    
    # Respond with success message
    return jsonify({'message': data}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")