import time
import uuid
import threading
from flask import Flask, jsonify

app = Flask(__name__)

tasks = {}


def run_background_task(task_id):
    tasks[task_id]["status"] = "running"

    time.sleep(10)

    tasks[task_id]["status"] = "completed"
    tasks[task_id]["result"] = "Background task completed successfully"


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Background Tasks API is running"})


@app.route("/tasks/start", methods=["POST"])
def start_task():
    task_id = str(uuid.uuid4())

    tasks[task_id] = {
        "status": "pending",
        "result": None
    }

    thread = threading.Thread(target=run_background_task, args=(task_id,))
    thread.start()

    return jsonify({
        "message": "Background task started",
        "task_id": task_id
    }), 202


@app.route("/tasks/<task_id>", methods=["GET"])
def get_task_status(task_id):
    task = tasks.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "task_id": task_id,
        "status": task["status"],
        "result": task["result"]
    })


if __name__ == "__main__":
    app.run(debug=True)
