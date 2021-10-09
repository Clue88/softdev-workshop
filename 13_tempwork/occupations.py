# Clear Zebra: Christopher Liu, Emma Buller, Reng Zheng
# SoftDev
# K13 -- Template for Success
# 2021-10-08

import csv
import random


def read_occupations(filename: str) -> dict:
    """Reads a CSV file containing job classes and percentages and returns a
    dictionary with the job class as the key and the percentage as a float.
    Ignores the first header line and adds an 'Other' category for percentages
    outside of the 'Total'."""

    occupations = {}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)

        # We ignore the first header line with the column titles.
        next(reader)

        for row in reader:
            job_class = row[0]
            percentage = row[1]
            link = row[2]
            occupations[job_class] = {"percentage": float(percentage), "link": link}

    # We mark everything not in the occupations list as "Other".
    total_percentage = occupations["Total"]["percentage"]
    occupations["Other"] = {
        "percentage": round(100 - total_percentage, 2),
        "link": occupations["Total"]["link"],
    }
    del occupations["Total"]

    return occupations


def choose_from_dict(occupations: dict) -> str:
    """Picks an occupation randomly using the percentage weights in the given
    occupations dictionary."""

    job_classes = list(occupations.keys())
    percentages = list(
        value["percentage"] for value in occupations.values()
    )  # We extract only the percent data

    choice = random.choices(job_classes, weights=percentages)[0]
    return choice


def random_occupation(filename: str) -> str:
    """Returns a random occupation based on the job classes and percentage
    weights provided in the given CSV file."""

    occupations = read_occupations(filename)
    return choose_from_dict(occupations)


def main():
    print(random_occupation("data/occupations.csv"))


if __name__ == "__main__":
    main()
