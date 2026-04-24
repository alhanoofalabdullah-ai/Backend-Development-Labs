from flask import Flask, jsonify, request

app = Flask(__name__)

audit_logs = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Audit Log API is running"})


@app.route("/logs", methods=["GET"])
def get_logs():
    user = request.args.get("user")
    action = request.args.get("action")

    filtered_logs = audit_logs

    if user:
        filtered_logs = [
            log for log in filtered_logs
            if user.lower() in log["user"].lower()
        ]

    if action:
        filtered_logs = [
            log for log in filtered_logs
            if action.lower() in log["action"].lower()
        ]

    return jsonify(filtered_logs)


@app.route("/logs", methods=["POST"])
def create_log():
    global current_id

    data = request.get_json()

    user = data.get("user")
    action = data.get("action")
    details = data.get("details")

    if not user or not action or not details:
        return jsonify({
            "error": "User, action, and details are required"
        }), 400

    log = {
        "id": current_id,
        "user": user,
        "action": action,
        "details": details
    }

    audit_logs.append(log)
    current_id += 1

    return jsonify(log), 201


@app.route("/logs/<int:log_id>", methods=["GET"])
def get_log(log_id):
    log = next((l for l in audit_logs if l["id"] == log_id), None)

    if not log:
        return jsonify({"error": "Log not found"}), 404

    return jsonify(log)


@app.route("/logs/<int:log_id>", methods=["DELETE"])
def delete_log(log_id):
    global audit_logs

    log = next((l for l in audit_logs if l["id"] == log_id), None)

    if not log:
        return jsonify({"error": "Log not found"}), 404

    audit_logs = [
        l for l in audit_logs
        if l["id"] != log_id
    ]

    return jsonify({"message": "Log deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
