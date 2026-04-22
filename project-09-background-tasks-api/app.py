
## app.py

```python
import time
import threading
from flask import Flask, jsonify

app = Flask(__name__)


def background_task():
    print("Background task started...")
    time.sleep(5)
    print("Background task finished.")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Background Tasks API is running"}), 200


@app.route("/task", methods=["POST"])
def run_task():
    thread = threading.Thread(target=background_task)
    thread.start()

    return jsonify({"message": "Task started in background"}), 200


if __name__ == "__main__":
    app.run(debug=True)
