from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Order Management API is running"})


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():
    global current_id

    data = request.get_json()

    customer_name = data.get("customer_name")
    product_name = data.get("product_name")
    quantity = data.get("quantity")
    total_price = data.get("total_price")

    if not customer_name or not product_name or quantity is None or total_price is None:
        return jsonify({"error": "Customer name, product name, quantity, and total price are required"}), 400

    order = {
        "id": current_id,
        "customer_name": customer_name,
        "product_name": product_name,
        "quantity": quantity,
        "total_price": total_price,
        "status": "pending"
    }

    orders.append(order)
    current_id += 1

    return jsonify(order), 201


@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order)


@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()

    order["customer_name"] = data.get("customer_name", order["customer_name"])
    order["product_name"] = data.get("product_name", order["product_name"])
    order["quantity"] = data.get("quantity", order["quantity"])
    order["total_price"] = data.get("total_price", order["total_price"])

    return jsonify(order)


@app.route("/orders/<int:order_id>/status", methods=["PATCH"])
def update_order_status(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    status = data.get("status")

    if not status:
        return jsonify({"error": "Status is required"}), 400

    allowed_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]

    if status not in allowed_statuses:
        return jsonify({"error": "Invalid order status"}), 400

    order["status"] = status

    return jsonify({
        "message": "Order status updated successfully",
        "order": order
    })


@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    global orders

    order = next((o for o in orders if o["id"] == order_id), None)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    orders = [o for o in orders if o["id"] != order_id]

    return jsonify({"message": "Order deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
