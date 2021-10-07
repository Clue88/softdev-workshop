# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# Q0: What happens if you remove render_template from this line?
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "No hablo queso!"


coll = [0, 1, 1, 2, 3, 5, 8]


# Q1: Can all of your teammates confidently predict the URL to use to load this page?
@app.route("/my_foist_template")
def test_tmplt():
    # Q2: What is the significance of each argument?
    return render_template("model_tmplt.html", foo="chris is cool", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
