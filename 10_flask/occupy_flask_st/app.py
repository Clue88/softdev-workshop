# STD Trio: Christopher Liu, Tina Nguyen, Tami Takada
# SoftDev
# K10 -- Occupation Selector Flask App
# 2021-10-04

from flask import Flask

import occupations

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def display_occupation():
    output = "STD Trio: Christopher Liu, Tina Nguyen, Tami Takada</br></br>"

    jobs = occupations.read_occupations("occupations.csv")
    output += "<strong>Selected Job:</strong> "
    output += occupations.choose_from_dict(jobs) + "</br></br>"

    output += "<strong>List of Jobs:</strong></br>"
    for job in jobs.keys():
        output += job + "</br>"

    return output

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
