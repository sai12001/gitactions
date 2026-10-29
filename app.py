import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)


def status_payload():
    return {
        "message": os.environ.get(
            "APP_MESSAGE",
            "Hello from AWS EKS and AWS Fargate!",
        ),
        "deployment": os.environ.get("APP_DEPLOYMENT", "GitHub Actions"),
        "version": os.environ.get("APP_VERSION", "v5"),
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    return jsonify(status_payload())


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
