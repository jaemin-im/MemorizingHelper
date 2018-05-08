import sqlite3
import datetime

con = sqlite3.connect("./term.db")
cursor = con.cursor()

def addterm():
    print("You should input the term and mean.")
    term = str(input("Input the term: "))
    mean = str(input("Input the mean: "))
    date = str((datetime.datetime.now()).strftime('%Y%m%d'))
    try:
        cursor.execute("INSERT INTO term VALUES(\"{}\", \"{}\", \"{}\", {}, {})".format(date, term, mean, 0, 0))
    except:
        print("Error has occured while adding term to database.")
        return
    print('Added {}: {} (Marked: {}, Memorized: {}) on {}'.format(term, mean, 0, 0, date))