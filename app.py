from flask import Flask, redirect, render_template, request, jsonify, session, url_for
from account import *
from survey_trends import *
from datetime import datetime  # Import datetime for getting today's date
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

@app.route('/register', methods=['GET'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))  # Redirect to the home page if logged in
    return render_template('register.html')

@app.route('/home', methods=['GET'])
def home():
    # Check if user data exists in session
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    
    # If session exists, render the home page
    return render_template('admin-home.html')

@app.route('/thank_you')
def thank_you():
    # Check if user data exists in session
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in
    # If session exists, render the home page
    return render_template('/thank_u.html')

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
    
    user_id = session.get('user_id')  # Get the user ID from the session
    survey = Survey()
    user_submitted = survey.user_has_submitted(user_id) if user_id else False
    previous_response = survey.get_user_response(user_id) if user_id else None
    return render_template('trends.html', user_submitted=user_submitted, previous_response=previous_response)

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

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    response = request.form.get('supportOption')
    survey_date = datetime.today().date()  # Get today's date
    user_id = session['user_id']
    survey = Survey()
    survey.insert_response(response, user_id, survey_date)  # Pass the response and date
    return redirect(url_for('thank_you'))

@app.route('/monthly-survey-statistics', methods=['GET'])
def monthly_survey_statistics():
    """
    Endpoint to get monthly survey response percentages for the year 2024.
    """
    survey = Survey()  # Initialize the Survey class
    monthly_percentages = survey.get_monthly_response_percentage_2024()  # Call the method
    return jsonify(monthly_percentages)  # Return the results as JSON

@app.route('/response-percentage', methods=['GET'])
def response_percentage():
    """Endpoint to get the percentage of Emergency Needs and Livelihood Support responses."""
    percentages = Survey().get_response_percentage()  # Call your method
    return jsonify(percentages)  # Return as JSON

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")