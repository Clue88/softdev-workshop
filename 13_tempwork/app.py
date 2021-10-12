# Clear Zebra: Christopher Liu, Emma Buller, Reng Zheng
# SoftDev
# K13 -- Template for Success
# 2021-10-08

from flask import Flask, render_template

import occupations

app = Flask(__name__)


@app.route("/occupyflaskst")
def occupyflaskst() -> str:
    """Reads in occupations data, chooses a random occupation, and displays the
    random occupation and occupations data in an HTML table."""
    jobs = occupations.read_occupations("data/occupations.csv")
    random_occupation = occupations.choose_from_dict(jobs)

    return render_template(
        "tablified.html", jobs=jobs, random_occupation=random_occupation
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
