import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify(error="Please pass city"), 400

    api_key = os.environ.get("b22578171a9174641c32ffd1416c4f5c")
    if not api_key:
        return jsonify(error="OPENWEATHER_API_KEY not configured"), 500

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return (resp.text, resp.status_code, {"Content-Type": "application/json"})