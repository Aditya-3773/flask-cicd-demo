from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return jsonify({
        "project": "Task Manager API",
        "status": "Running"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    # Validate request body
    if not data or "title" not in data:
        return jsonify({"message": "Title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def complete_task(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            return jsonify(task), 200

    return jsonify({"message": "Task not found"}), 404


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200

    return jsonify({"message": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)