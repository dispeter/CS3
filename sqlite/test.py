import sqlite3
import random
db = sqlite3.connect("test.db")

cursor = db.cursor()

# cursor.execute("CREATE TABLE profile(id INTEGER, firstname TEXT, lastname TEXT)")

names = ["Ekko" , "Pete" , "Neel" , "Maxine"]
for name in names:
    cursor.execute('''
        INSERT INTO profile(id , firstname , lastname)
                    values(?,?,?)''',(random.randint(1,100),name,"Erg"))

db.commit()
db.close()