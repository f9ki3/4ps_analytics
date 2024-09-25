from flask import Flask, redirect, render_template, request, jsonify, session, url_for
from account import *

app = Flask(__name__)
app.secret_key = '4psjasgasuqh'

@app.route('/', methods=['GET'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))  # Redirect to the home page if logged in
    
    return render_template('login.html')  # Changed to show login form if not logged in

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login'))  # Redirect to the login page after logging out

@app.route('/login', methods=['GET'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))  # Redirect to the home page if logged in
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    # Check if user data exists in session
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    
    # If session exists, render the home page
    return render_template('admin-home.html')

@app.route('/about', methods=['GET'])
def about():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    
    # If session exists, render the about page
    return render_template('about.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Check if user data exists in session
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    
    return render_template('dashboard.html')

@app.route('/trends', methods=['GET'])
def trends():
    # Check if user data exists in session
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    
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

@app.route('/loginAccount', methods=['POST'])
def loginAccount():
    # Get data from the request
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Call the login_account method from Accounts class
    result = Accounts().login_account(email, password)

    if result['success']:  # Check the success status
        # Store all user information in session
        user_data = result['data']
        session['user_id'] = user_data['id']
        session['first_name'] = user_data['first_name']
        session['last_name'] = user_data['last_name']
        session['address'] = user_data['address']
        session['gender'] = user_data['gender']
        session['birthday'] = user_data['birthday']
        session['contact_number'] = user_data['contact_number']
        session['email'] = user_data['email']  # Store email if needed
        
        return jsonify({'success': True, 'message': 'Login successful', 'data': user_data}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid email or password.'}), 401

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")