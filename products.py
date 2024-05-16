from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def products():
    #username = request.args.get('username')
    #if username in logged_in_users:
   return send_from_directory('templates', 'products.html')
    #return jsonify({'message': 'Unauthorized access to products microservice.'}), 401

if __name__ == "__main__":
   # logged_in_users = {"user1": True, "user2": True}  # Simulating logged in users
    app.run(host="0.0.0.0", port=5002, debug=True)

