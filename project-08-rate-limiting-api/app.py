
## app.py

```python
from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Rate Limiting API is running"}), 200


@app.route("/limited", methods=["GET"])
@limiter.limit("5 per minute")
def limited():
    return jsonify({"message": "This endpoint is rate limited"}), 200


if __name__ == "__main__":
    app.run(debug=True)
