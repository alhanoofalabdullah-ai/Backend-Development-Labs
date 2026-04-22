from flask import Flask, request, jsonify

app = Flask(__name__)

users = []


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    role = data.get("role")

    if not name or not role:
        return jsonify({"error": "Both name and role are required"}), 400

    user = {
        "id": len(users),
        "name": name,
        "role": role
    }

    users.append(user)
    return jsonify({"message": "User added successfully", "user": user}), 201


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully", "user": user}), 200

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
