
## app.py

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "category": "electronics"},
    {"id": 2, "name": "Phone", "category": "electronics"},
    {"id": 3, "name": "Chair", "category": "furniture"},
    {"id": 4, "name": "Table", "category": "furniture"},
    {"id": 5, "name": "Headphones", "category": "electronics"}
]


@app.route("/products", methods=["GET"])
def get_products():
    name = request.args.get("name")
    category = request.args.get("category")

    filtered_products = products

    if name:
        filtered_products = [
            product for product in filtered_products
            if name.lower() in product["name"].lower()
        ]

    if category:
        filtered_products = [
            product for product in filtered_products
            if product["category"].lower() == category.lower()
        ]

    return jsonify(filtered_products), 200


if __name__ == "__main__":
    app.run(debug=True)
