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

def modterm():
    pass

def practerm():
    pass

def testterm():
    pass

def searchterm():
    print("You should input the term to search.")
    term = str(input("input the term: "))
    try:
        cursor.execute("SELECT * FROM term WHERE Term=\'{}\'".format(term))
        result = cursor.fetchall()
    except:
        print("Error has occured while searching term in database.")
        return
    print('Found {}!'.format(result))
