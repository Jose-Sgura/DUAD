from flask import Flask, jsonify, request
import json
import os


app = Flask(__name__)

JSON_FILE = "jobs.json"
STATUS = ["To do", "In process", "Completed"]

def read_jobs():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE,"r", encoding= "utf-8") as f:
        return json.load(f)

def write_jobs(jobs):
    with open(JSON_FILE,"w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent= 4)

@app.route("/jobs", methods = ["GET"])
def get_jobs():
    jobs = read_jobs()

    filter_status = request.args.get("status")
    if filter_status:
        if filter_status not in STATUS:
            return jsonify({"error": f"Invalid status. options: {STATUS}"}), 400
        jobs = [j for j in jobs if j["status"]== filter_status]
    return jsonify(jobs), 200

@app.route("/jobs/<int:id>", methods=["GET"])
def get_job(id):
    jobs = read_jobs()
    job = next((j for j in jobs if j["id"]==id), None)
    if job is None:
        return jsonify({"error":"Job was not found"}),404
    return jsonify(job),200

@app.route("/jobs", methods = ["POST"])
def make_job():
    jobs=read_jobs()
    data = request.get_json()

    if not data:
        return jsonify({"error": "there is not data"}), 400
    
    new_id = data.get("id")
    if new_id is None:
        return jsonify({"error":"The identifier is a must"})
    if any(j["id"]== new_id for j in jobs):
        return jsonify({"error":f"The job with the identifier {new_id} already exists"}),400
    
    if not data.get("title"):
        return jsonify({"error":"Title is a must"}),400
    if not data.get("description"):
        return jsonify({"error":"Description is a must"}),400
    if not data.get("status"):
        return jsonify({"error":"Status is a must"}),400
    if data["status"] not in STATUS:
        return jsonify({"error": f"the status is invalid. options {STATUS} "}), 400
    
    new_job = {
        "id": new_id,
        "title": data["title"],
        "description": data["description"],
        "status":data["status"]

    }

    jobs.append(new_job)
    write_jobs(jobs)

    return jsonify(new_job),201
@app.route("/jobs/<int:id>", methods = ["PUT"])
def update_jobs(id):
    jobs = read_jobs()
    job = next((j for j in jobs if j["id"]==id), None)

    if job is None:
        return jsonify({"error":"The jobs is not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error":"data was not sent"}), 400
    
    if "title" in data:
        if not data["title"]:
            return jsonify({"error": "Title cannot be empty"}),400
        job["title"] = data["title"]
    
    if "description" in data:
        if not data["description"]:
            return({"error":"Description cannot be empty"}),400
        job["description"] = data ["description"]
    
    if "status" in data:
        if not data["status"]:
            return jsonify({"error":"Status cannot be empty"}),400
        if data["status"] not in STATUS:
            return jsonify({"error": f"Status invalid. options {STATUS}"}), 400
        job["status"] = data["status"]

    write_jobs(jobs)
    return jsonify(job),200

@app.route("/jobs/<int:id>", methods = ["DELETE"])
def delete_job(id):
    jobs = read_jobs()
    job = next((j for j in jobs if j["id"]== id), None)

    if job is None:
        return jsonify({"error": "The job was not found"}),404
    updated_jobs = [j for j in jobs if j["id"]!=id]
    write_jobs(updated_jobs)

    return jsonify({"message":f"The job {id} deleted correctly"}),200
        

if __name__ == "__main__":
    app.run(host="localhost", debug=True)