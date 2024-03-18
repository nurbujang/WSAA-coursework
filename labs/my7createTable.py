# use 127.0.0.1

import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="wsaa4"
)

cursor = db.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

cursor.execute(sql)

db.close()
cursor.close()

#mysql:
# show tables; (will have student table)
# desc student;

# now go to my7insertIntoTest


######################################################################
# this doesnt work


# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="wsaa"
# )

# cursor = db.cursor()
# sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), age INT)"

# cursor.execute(sql)

# db.close()
# cursor.close()