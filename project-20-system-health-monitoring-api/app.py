from flask import Flask, jsonify
import random

app = Flask(__name__)

system_status = {
    "cpu_usage": "35%",
    "memory_usage": "58%",
    "disk_usage": "72%",
    "service_status": "running"
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "System Health Monitoring API is running"
    })


@app.route("/health", methods=["GET"])
def get_health():
    return jsonify(system_status)


@app.route("/health/refresh", methods=["POST"])
def refresh_health():
    system_status["cpu_usage"] = f"{random.randint(20, 90)}%"
    system_status["memory_usage"] = f"{random.randint(30, 95)}%"
    system_status["disk_usage"] = f"{random.randint(40, 98)}%"

    return jsonify({
        "message": "System health refreshed successfully",
        "system_status": system_status
    })


@app.route("/health/service", methods=["PATCH"])
def update_service_status():
    system_status["service_status"] = "running"

    return jsonify({
        "message": "Service status updated successfully",
        "system_status": system_status
    })


if __name__ == "__main__":
    app.run(debug=True)
