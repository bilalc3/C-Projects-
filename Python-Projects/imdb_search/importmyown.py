from cs50 import SQL
import csv
from sys import argv, exit
import sqlite3

open(f"students.db", "w").close()
db = SQL("sqlite:///students.db")

#db.execute =("Query")

#db.execute("CREATE TABLE shows (first TEXT, middle TEXT, last TEXT, house TEXT,birth NUMERIC)")

if (len(argv) != 2):
    print ("Enter 1 csv file needed")
    exit

with open (argv[1] ,"r") as file:  #characters.csv
    reader = csv.DictReader(file)

    for row in reader:
        namelist = []
        namelist = row["name"].split()
        namelen = len(row["name"].split())
        print (namelen)

        if namelen == 2:
            firstname = namelist[0]
            lastname = namelist[1]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", namelist[0] ,None, namelist[1], row["house"], row["birth"])

        elif namelen == 3:
            firstname = namelist[0]
            middlename = namelist [1]
            lastname = namelist [2]
            db.execute("INSERT into students(first, middle, last, house, birth) VALUES (?,?,?,?,?)", firstname, middlename, lastname, row["house"], row["birth"])






#db.execute("INSERT into students(first, middle, last, house, birth) VALUES (?,?,?,?,?)", row["name"], row["house"], row["birth"]

