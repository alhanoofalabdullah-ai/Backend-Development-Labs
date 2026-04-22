
---

## 🧠 app.py

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "Name and price are required"}), 400

    item = {
        "id": len(items),
        "name": name,
        "price": price
    }

    items.append(item)

    return jsonify({
        "message": "Item created successfully",
        "item": item
    }), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])

            return jsonify({
                "message": "Item updated successfully",
                "item": item
            }), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({
                "message": "Item deleted successfully",
                "item": item
            }), 200

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
