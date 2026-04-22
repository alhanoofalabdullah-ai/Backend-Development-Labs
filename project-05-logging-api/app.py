
## app.py

```python
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/", methods=["GET"])
def home():
    logging.info("Home endpoint accessed")
    return jsonify({"message": "Logging API is running"}), 200


@app.route("/log", methods=["POST"])
def log_message():
    data = request.get_json()

    if not data or "message" not in data:
        logging.warning("Invalid log request received")
        return jsonify({"error": "Message is required"}), 400

    message = data["message"]
    logging.info(f"User message logged: {message}")

    return jsonify({
        "message": "Log saved successfully",
        "logged_message": message
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
