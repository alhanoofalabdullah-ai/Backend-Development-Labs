from flask import Flask, jsonify, request

app = Flask(__name__)

tickets = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Ticket Management API is running"})


@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(tickets)


@app.route("/tickets", methods=["POST"])
def create_ticket():
    global current_id

    data = request.get_json()

    title = data.get("title")
    description = data.get("description")
    priority = data.get("priority", "medium")

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    allowed_priorities = ["low", "medium", "high", "critical"]

    if priority not in allowed_priorities:
        return jsonify({"error": "Invalid priority"}), 400

    ticket = {
        "id": current_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }

    tickets.append(ticket)
    current_id += 1

    return jsonify(ticket), 201


@app.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    return jsonify(ticket)


@app.route("/tickets/<int:ticket_id>/assign", methods=["PATCH"])
def assign_ticket(ticket_id):
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    data = request.get_json()
    agent = data.get("agent")

    if not agent:
        return jsonify({"error": "Agent name is required"}), 400

    ticket["assigned_to"] = agent

    return jsonify({
        "message": "Ticket assigned successfully",
        "ticket": ticket
    })


@app.route("/tickets/<int:ticket_id>/priority", methods=["PATCH"])
def update_priority(ticket_id):
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    data = request.get_json()
    priority = data.get("priority")

    allowed_priorities = ["low", "medium", "high", "critical"]

    if priority not in allowed_priorities:
        return jsonify({"error": "Invalid priority"}), 400

    ticket["priority"] = priority

    return jsonify({
        "message": "Ticket priority updated successfully",
        "ticket": ticket
    })


@app.route("/tickets/<int:ticket_id>/status", methods=["PATCH"])
def update_status(ticket_id):
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    data = request.get_json()
    status = data.get("status")

    allowed_statuses = ["open", "in_progress", "resolved", "closed"]

    if status not in allowed_statuses:
        return jsonify({"error": "Invalid status"}), 400

    ticket["status"] = status

    return jsonify({
        "message": "Ticket status updated successfully",
        "ticket": ticket
    })


@app.route("/tickets/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    global tickets

    ticket = next((t for t in tickets if t["id"] == ticket_id), None)

    if not ticket:
        return jsonify({"error": "Ticket not found"}), 404

    tickets = [t for t in tickets if t["id"] != ticket_id]

    return jsonify({"message": "Ticket deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
