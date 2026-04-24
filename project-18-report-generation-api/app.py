from flask import Flask, jsonify, request

app = Flask(__name__)

reports = []
current_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Report Generation API is running"})


@app.route("/reports", methods=["GET"])
def get_reports():
    return jsonify(reports)


@app.route("/reports", methods=["POST"])
def create_report():
    global current_id

    data = request.get_json()

    report_name = data.get("report_name")
    report_type = data.get("report_type")

    if not report_name or not report_type:
        return jsonify({"error": "Report name and report type are required"}), 400

    report = {
        "id": current_id,
        "report_name": report_name,
        "report_type": report_type,
        "status": "pending"
    }

    reports.append(report)
    current_id += 1

    return jsonify(report), 201


@app.route("/reports/<int:report_id>", methods=["GET"])
def get_report(report_id):
    report = next((r for r in reports if r["id"] == report_id), None)

    if not report:
        return jsonify({"error": "Report not found"}), 404

    return jsonify(report)


@app.route("/reports/<int:report_id>/status", methods=["PATCH"])
def update_report_status(report_id):
    report = next((r for r in reports if r["id"] == report_id), None)

    if not report:
        return jsonify({"error": "Report not found"}), 404

    data = request.get_json()
    status = data.get("status")

    allowed_statuses = ["pending", "processing", "completed", "failed"]

    if status not in allowed_statuses:
        return jsonify({"error": "Invalid report status"}), 400

    report["status"] = status

    return jsonify({
        "message": "Report status updated successfully",
        "report": report
    })


@app.route("/reports/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):
    global reports

    report = next((r for r in reports if r["id"] == report_id), None)

    if not report:
        return jsonify({"error": "Report not found"}), 404

    reports = [r for r in reports if r["id"] != report_id]

    return jsonify({"message": "Report deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
