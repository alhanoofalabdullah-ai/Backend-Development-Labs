
## app.py

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = "database.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role FROM users")
    rows = cursor.fetchall()
    conn.close()

    users = [{"id": row[0], "name": row[1], "role": row[2]} for row in rows]
    return jsonify(users), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        user = {"id": row[0], "name": row[1], "role": row[2]}
        return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    role = data.get("role")

    if not name or not role:
        return jsonify({"error": "Both name and role are required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, role) VALUES (?, ?)", (name, role))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": user_id,
            "name": name,
            "role": role
        }
    }), 201


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"error": "User not found"}), 404

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
