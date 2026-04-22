
## app.py

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Both username and password are required"}), 400

    for user in users:
        if user["username"] == username:
            return jsonify({"error": "Username already exists"}), 409

    user = {
        "id": len(users),
        "username": username,
        "password": password
    }

    users.append(user)

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user["id"],
            "username": user["username"]
        }
    }), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Both username and password are required"}), 400

    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)
