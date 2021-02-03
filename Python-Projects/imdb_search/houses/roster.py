# TODO
#SELECT first, middle, last, birth from students where house = "Gryffindor" ORDER BY last, first;
from cs50 import SQL
import csv
from sys import argv, exit
import sqlite3
import cs50

if (len(argv) != 2):
    print ("Enter 1 csv file needed")
    exit(1)
db = cs50.SQL("sqlite:///students.db")

house = argv[1]
print (house)

rows= {}
rows =db.execute ("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house);

for row in rows:
    first = row['first']
    middle = row['middle']
    last = row['last']
    birth = row['birth']
    if middle == None:
         print (f"{first} {last} born: {birth}")
    else:
        print (f"{first} {middle} {last} born: {birth}")



