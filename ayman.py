import sqlite3
import csv

file = "discobandit.db"

db = sqlite3.connect(file) #open if f exists, otherwise create
cur = db.cursor()    #facilitate db ops

selectStatement = "SELECT name, mark from students, courses WHERE students.id = courses.id"

data = cur.execute(selectStatement)

curStudent = ""
avg = 0
ctr = 0

for student in data:
    if (student[0] == curStudent or curStudent == ""):
        curStudent = student[0]
        ctr += 1
        avg += student[1]
    else:
        print "%s has a %d average"%(curStudent, avg / ctr)
        ctr = 0
        avg = 0
        curStudent = ""
print "ayman has a SELECT mark FROM students WHERE mark < 65 gpa"
