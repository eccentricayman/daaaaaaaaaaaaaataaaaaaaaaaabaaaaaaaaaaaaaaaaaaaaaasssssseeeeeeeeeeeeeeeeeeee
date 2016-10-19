import sqlite3
import csv

file = "discobandit.db"

db = sqlite3.connect(file) #open if f exists, otherwise create
cur = db.cursor()    #facilitate db ops

selectStatement = "SELECT name, mark from students, courses WHERE students.id = courses.id"

data = cur.execute(selectStatement)

curStudent = ""
ctr = 0
avg = 0

for student in data:
    if curStudent == "":
        curStudent = student[0]
        avg = student[1]
        ctr = 1
    elif student[0] == curStudent:
        ctr += 1
        avg += student[1]
    elif student[0] != curStudent and curStudent != "":
        print "%s has a %d average"%(curStudent, avg / ctr)
        curStudent = student[0]
        ctr = 1
        avg = student[1]
        
