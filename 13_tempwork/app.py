# Clear Zebra: Christopher Liu, Emma Buller, Reng Zheng
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template

import occupations

app = Flask(__name__)


@app.route("/occupyflaskst")
def occupyflaskst():
    pass


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    app.run()
