# how to use python to interact with a mysql database
# in console, if there is already wsaa, drop database wsaa;

import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

cursor = db.cursor()

cursor.execute("create DATABASE wsaa4")

db.close()
cursor.close()

#mysql: show databases;
# show tables; (empty set)

# now go to my7createTable.py

############################################################################

#this had error

# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# cursor = db.cursor()

# cursor.execute("create DATABASE wsaa3")

# db.close()
# cursor.close()