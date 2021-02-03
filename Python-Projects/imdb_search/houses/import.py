from cs50 import SQL
import csv
from sys import argv, exit
import sqlite3
import cs50



if (len(argv) != 2):
    print ("Enter 1 csv file needed")
    exit(1)
db = cs50.SQL("sqlite:///students.db")


def breakname(name):
    names = name.split()
    return names if len (names)>= 3 else [names[0], None, names[1]]
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")


csvpath = argv [1]

with open ("characters.csv", "r") as file:  #characters.csv
    reader = csv.DictReader(file)
    for row in reader:
        namesnew = breakname(row["name"])
        db.execute ("INSERT INTO students (first, middle, last, house, birth) VALUES(?,?,?,?,?)",namesnew[0], namesnew[1], namesnew[2], row["house"], row["birth"])



#db.execute("INSERT into students(first, middle, last, house, birth) VALUES (?,?,?,?,?)", row["name"], row["house"], row["birth"]

