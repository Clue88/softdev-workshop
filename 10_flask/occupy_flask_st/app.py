# STD Trio: Christopher Liu, Tina Nguyen, Tami Takada
# SoftDev
# K10 -- Occupation Selector Flask App
# 2021-10-04

from flask import Flask

# Import methods from occupations.py
import occupations

# Create instance of the Flask class
app = Flask(__name__)


@app.route("/") # Assign function to route
def display_occupation():
    # Print out trio name and roster and skips two lines
    output = "STD Trio: Christopher Liu, Tina Nguyen, Tami Takada</br></br>"

    # Creates dictionary called jobs which is a dictionary returned
    # from read_occupations() which reads through occupations.csv and makes the
    # keys job occupations and the values the percentages associated with it
    jobs = occupations.read_occupations("occupations.csv")

    output += "<strong>Selected Job:</strong> "
    # The randomly chosen job will be printed after this string
    output += occupations.choose_from_dict(jobs) + "</br></br>"
    # This prints out a randomly chosen occupation (weighted by the percents)
    # that is returned from choose_from_dict() and skips two lines


    output += "<strong>List of Jobs:</strong></br>"
    # Precedes a printed list of all the jobs in occupations.csv
    for job in jobs.keys():
    # Loops through all the keys in the dictionary and prints the job out,
    # going to the next line each time it prints
        output += job + "</br>"

    return output


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    app.run()
