"""
Clivan -- Christopher Liu, Ivan Mijacika
SoftDev pd0
K19 -- NASA Open APIs
2021-11-23
"""

import requests

from flask import Flask, render_template

app = Flask(__name__)


with open("key_nasa.txt", "r", encoding="utf-8") as api_file:
    NASA_API_KEY = api_file.read().strip()


@app.route("/")
def main():
    """Displays the NASA Astronomy Picture of the Day and the associated
    description."""

    api_request = requests.get(
        "https://api.nasa.gov/planetary/apod", params={"api_key": NASA_API_KEY}
    )
    if api_request.status_code == 200:
        img_url = api_request.json()["hdurl"]
        img_text = api_request.json()["explanation"]
        return render_template("main.html", img_url=img_url, img_text=img_text)

    return render_template("main.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
