from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Notification Management API is running"})


@app.route("/notifications", methods=["GET"])
def get_notifications():
    unread = request.args.get("unread")

    if unread == "true":
        unread_notifications = [
            notification for notification in notifications
            if notification["read"] is False
        ]
        return jsonify(unread_notifications)

    return jsonify(notifications)


@app.route("/notifications", methods=["POST"])
def create_notification():
    global current_id

    data = request.get_json()

    title = data.get("title")
    message = data.get("message")
    notification_type = data.get("type", "info")

    if not title or not message:
        return jsonify({"error": "Title and message are required"}), 400

    allowed_types = ["info", "warning", "error", "success"]

    if notification_type not in allowed_types:
        return jsonify({"error": "Invalid notification type"}), 400

    notification = {
        "id": current_id,
        "title": title,
        "message": message,
        "type": notification_type,
        "read": False
    }

    notifications.append(notification)
    current_id += 1

    return jsonify(notification), 201


@app.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification(notification_id):
    notification = next(
        (n for n in notifications if n["id"] == notification_id),
        None
    )

    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify(notification)


@app.route("/notifications/<int:notification_id>/read", methods=["PATCH"])
def mark_as_read(notification_id):
    notification = next(
        (n for n in notifications if n["id"] == notification_id),
        None
    )

    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    notification["read"] = True

    return jsonify({
        "message": "Notification marked as read",
        "notification": notification
    })


@app.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    global notifications

    notification = next(
        (n for n in notifications if n["id"] == notification_id),
        None
    )

    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    notifications = [
        n for n in notifications
        if n["id"] != notification_id
    ]

    return jsonify({"message": "Notification deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
