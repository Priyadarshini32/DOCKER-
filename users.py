from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Simulated user database with hardcoded passwords
users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"}
}

logged_in_users = {}  # Keep track of logged in users

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username]['password'] == password:
            logged_in_users[username] = True
            return redirect('http://13.211.33.165:5002/products')

        return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    username = request.form.get('username')
    if username in logged_in_users:
        del logged_in_users[username]
        return jsonify({'message': 'Logged out successfully'})
    return jsonify({'message': 'User not logged in'}), 401

@app.route('/users')
def list_users():
    return jsonify({'message': 'This is the users microservice.'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

