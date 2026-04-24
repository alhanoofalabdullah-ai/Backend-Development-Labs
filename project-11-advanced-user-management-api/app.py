from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
next_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Advanced User Management API is running"})


@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    role = data.get("role", "user")

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    user = {
        "id": next_id,
        "username": username,
        "email": email,
        "role": role,
        "active": True
    }

    users.append(user)
    next_id += 1

    return jsonify({"message": "User created successfully", "user": user}), 201


@app.route("/users", methods=["GET"])
def get_users():
    search = request.args.get("search")

    if search:
        filtered_users = [
            user for user in users
            if search.lower() in user["username"].lower()
        ]
        return jsonify(filtered_users)

    return jsonify(users)


@app.route("/users/<int:user_id>/role", methods=["PUT"])
def update_role(user_id):
    data = request.get_json()
    new_role = data.get("role")

    if not new_role:
        return jsonify({"error": "Role is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["role"] = new_role
            return jsonify({"message": "User role updated", "user": user})

    return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>/status", methods=["PUT"])
def update_status(user_id):
    data = request.get_json()
    active = data.get("active")

    if active is None:
        return jsonify({"error": "Active status is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["active"] = active
            return jsonify({"message": "User status updated", "user": user})

    return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"})

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
