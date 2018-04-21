#!/usr/bin/env python3



from requests import get

import json,csv

import sqlite3



q={'symbol':'AAPL'}

s = "http://dev.markitondemand.com/Api/v2/Quote/json/"

res = get(s,q)

r = res.json()

ke=list(r.keys())

va=list(r.values())
print(r)


print("keys ",ke)

print(va)



conn=sqlite3.connect('markit.db')

conn.execute('''CREATE TABLE IF NOT EXISTS Maark(Id INT PRIMARY KEY)''')

print("Adding first row ",ke[0],va[0])





# Start the for loop from here



conn.execute("ALTER TABLE Maark ADD COLUMN {} ;".format(ke[0]))

conn.execute("INSERT INTO Maark ({}) VALUES('{}');".format(ke[0],va[0]))



for i in range(1,len(ke)-1):

	print("Adding ",ke[i],va[i])

	conn.execute("ALTER TABLE Maark ADD COLUMN {} ;".format(ke[i]))

	print(ke[i],va[i])

	conn.execute("UPDATE Maark SET '{}'='{}';".format(ke[i],va[i]))

conn.commit()
