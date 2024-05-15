from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Simulated user database
users = {
    "user1": {"password": "pw1"},
    "user2": {"password": "pw2"}
}

logged_in_users = {}  # Keep track of logged in users

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username]['password'] == password:
        logged_in_users[username] = True
        return redirect(url_for('products'))

    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    username = request.json.get('username')
    if username in logged_in_users:
        del logged_in_users[username]
        return jsonify({'message': 'Logged out successfully'})
    return jsonify({'message': 'User not logged in'}), 401

@app.route('/users')
def list_users():
    return jsonify({'message': 'This is the users microservice.'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
