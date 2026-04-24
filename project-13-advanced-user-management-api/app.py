from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Advanced User Management API is running"})


@app.route("/users", methods=["GET"])
def get_users():
    name = request.args.get("name")
    email = request.args.get("email")

    filtered_users = users

    if name:
        filtered_users = [
            user for user in filtered_users
            if name.lower() in user["name"].lower()
        ]

    if email:
        filtered_users = [
            user for user in filtered_users
            if email.lower() in user["email"].lower()
        ]

    return jsonify(filtered_users)


@app.route("/users", methods=["POST"])
def create_user():
    global current_id

    data = request.get_json()

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    user = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(user)
    current_id += 1

    return jsonify(user), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return jsonify(user)


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users

    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]

    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
