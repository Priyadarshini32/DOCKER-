from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Sample product data
products_data = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 30}
]

logged_in_users = {}  # Keep track of logged in users

@app.route('/products')
def products():
    if request.headers.get('Referer') and 'login' not in request.headers.get('Referer'):
        username = request.args.get('username')
        if username in logged_in_users:
            return jsonify({'products': products_data})
    return jsonify({'message': 'Unauthorized access to products microservice.'}), 401

def run_products_service():
    app.run(host="0.0.0.0", port=5002, debug=True)

if __name__ == "__main__":
    products_thread = threading.Thread(target=run_products_service)
    products_thread.start()
