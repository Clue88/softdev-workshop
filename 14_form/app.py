# CircleTable - Yusuf Elsharawy, Christopher Liu, Naomi Naranjo
# SoftDev
# K14 -- Form and Function
# 2021-10-14

from flask import Flask  # Facilitate flask webserving
from flask import render_template  # Facilitate jinja templating
from flask import request  # Facilitate form submission

# Create Flask object
app = Flask(__name__)


@app.route("/", methods=["GET"])
def disp_loginpage():
    """Returns the login page."""
    return render_template("login.html")


@app.route("/auth", methods=["GET"])
def authenticate():
    """Returns the responge page, including the username, request method, and
    greeting."""
    if app.debug:
        print("\n\n\n")
        print("***DIAG: this Flask obj ***")
        print(app)
        print("***DIAG: request obj ***")
        print(request)
        print("***DIAG: request.args ***")
        print(request.args)
    return render_template(
        "response.html", username=request.args["username"], method=request.method
    )


if __name__ == "__main__":  # False if this file imported as module
    # Enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
