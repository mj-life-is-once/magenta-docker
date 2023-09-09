import glob
import json
import logging
import os
import subprocess

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from gdrive import GDrive

app = Flask(__name__)
gd = GDrive("secret.json")

SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:5000/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Magenta Music Generator"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
CORS(app)


def scanAndUpload(path):
    logging.info("Scan %s: starting")
    latest_file_path = getMostRecentFile(path)
    # file_name = os.path.basename(latest_file_path)
    print(latest_file_path)
    response = gd.upload_file(file_name=latest_file_path)
    # if response["result"] == "OK":
    #     print("remove file from the path")
    #     os.remove(latest_file_path)
    logging.info("Scan %s: finishing")
    return response


def getMostRecentFile(path):
    try:
        list_of_files = glob.glob(
            f"{path}/*"
        )  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
    except ValueError as e:
        print(e)
        return ""


@app.route("/generate")
def generate():
    parent_path = os.path.dirname(os.getcwd())
    target_path = f"{parent_path}/volume/magenta/generated/polyphony_rnn"
    subprocess.Popen(["chmod", "u+x", "generate.sh"])
    exit_code = subprocess.call("./generate.sh")
    print(exit_code)
    if not exit_code:
        result = scanAndUpload(target_path)
    # get the file id from the frontend when finished uploading the generated midi file
    # 1. create midi
    # 2. upload generated midi file to the server

    # download the most recent file from gdrive
    # latest_file_path = getMostRecentFile(target_path)
    # os.path.basename(latest_file_path)
    result = {"exit_code": exit_code}
    return f"<p>{result}</p>"


@app.route("/downloadFile")
def download():
    try:
        id = request.args.get("id")
        print(id)
        parent_path = os.path.dirname(os.getcwd())
        target_path = f"{parent_path}/volume/magenta/input/polyphony_rnn/melody.mid"

        result = gd.download_file(target_path)
    except Exception as e:
        print(e)
        result = {"result": e}
    return f"<p>{result}</p>"


@app.route("/uploadFile")
def drive():
    parent_path = os.path.dirname(os.getcwd())
    target_path = f"{parent_path}/volume/magenta/generated/polyphony_rnn"
    result = scanAndUpload(target_path)
    return f"<p>{result}</p>"


@app.route("/swagger.json")
def swagger():
    with open("swagger.json", "r") as f:
        return jsonify(json.load(f))


@app.route("/")
def hello_world():
    return "<p>Welcome to the Music Generator App</p>"


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
