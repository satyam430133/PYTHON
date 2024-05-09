# SQL Lite
# it contains connectin object for database connectivity 
import sqlite3 as database
connectionObj = database.connect("school.db")
cursorObj = connectionObj.cursor()
q = "CREATE TABLE student (RollNumber INTEGER NOT NULL, name TEXT NOT NULL, aadhar INTEGER PRIMARY KEY NOT NULL)"
q = "INSERT INTO student VALUES(101,'Ajay',90908088,'12th')"
q = "DELETE form student"
cursorObj.execute(q)
connectionObj.commit()