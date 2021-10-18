# CircleTable - Christopher Liu, Yusuf Elsharawy, Naomi Naranjo
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Displays a login page if the user is not logged in and a welcome page
    if the user is logged in."""

    return render_template("login.html")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    """Authenticates a log in request and either logs in or returns an error
    page."""

    # XXX HARDCODED USERNAME AND PASSWORD
    correct_username = "circletable"
    correct_password = "123456"

    # Check if username and password are correct
    username = request.form.get("username", default="")
    password = request.form.get("password", default="")


    if username == correct_username and password == correct_password:
        # Authentication success
        return render_template("response.html", username=request.form["username"])
    else:
        # Authentication failure
        return render_template("error.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
