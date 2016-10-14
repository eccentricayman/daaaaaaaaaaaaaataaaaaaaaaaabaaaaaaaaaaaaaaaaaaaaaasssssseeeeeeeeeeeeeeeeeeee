import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query

fPeeps = open("peeps.csv")
d = csv.DictReader(fPeeps)

for s in d:
    # INSERT INTO students VALUES(s[name], s[id])
    c.execute("INSERT INTO students VALUES(" + "\'" + s['name'] + "\'" + "," +  "\'" + s['id'] + "\'" + ")")

fPeeps.close()

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)

fCourses = open('courses.csv')
d = csv.DictReader(fCourses)

for s in d:
    # INSERT INTO courses VALUES (s[code],s[id],s[mark])
    c.execute("INSERT INTO courses VALUES(" + "\'" + s['code'] + "\'" + "," + "\'" + s['id'] + "\'" + "," + "\'" + s['mark'] + "\'" + ")")

#==========================================================
db.commit() #save changes
db.close()  #close database


