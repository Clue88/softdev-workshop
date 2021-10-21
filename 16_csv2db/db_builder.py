# CircleTable - Christopher Liu, Yusuf Elsharawy, Naomi Naranjo
# SoftDev
# K16 -- All About Database
# 2021-10-20

import sqlite3  # Enable control of an sqlite database
import csv  # Facilitate CSV I/O


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)  # Open if file exists, otherwise create
c = db.cursor()  # Facilitate db ops -- you will use cursor to trigger db events

# ==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = ""  # Test SQL stmt in sqlite3 shell, save as string
c.execute(command)  # Run SQL statement

# ==========================================================

db.commit()  # Save changes
db.close()  # Close database
