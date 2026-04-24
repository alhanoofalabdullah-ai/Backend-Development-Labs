from flask import Flask, jsonify, request

app = Flask(__name__)

products = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Product Inventory API is running"})


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products", methods=["POST"])
def create_product():
    global current_id

    data = request.get_json()

    name = data.get("name")
    category = data.get("category")
    quantity = data.get("quantity")
    price = data.get("price")

    if not name or not category or quantity is None or price is None:
        return jsonify({"error": "Name, category, quantity, and price are required"}), 400

    product = {
        "id": current_id,
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }

    products.append(product)
    current_id += 1

    return jsonify(product), 201


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()

    product["name"] = data.get("name", product["name"])
    product["category"] = data.get("category", product["category"])
    product["quantity"] = data.get("quantity", product["quantity"])
    product["price"] = data.get("price", product["price"])

    return jsonify(product)


@app.route("/products/<int:product_id>/stock", methods=["PATCH"])
def update_stock(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    quantity = data.get("quantity")

    if quantity is None:
        return jsonify({"error": "Quantity is required"}), 400

    product["quantity"] = quantity

    return jsonify({
        "message": "Stock updated successfully",
        "product": product
    })


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    products = [p for p in products if p["id"] != product_id]

    return jsonify({"message": "Product deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
