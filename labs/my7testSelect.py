import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="wsaa4"
)

cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)
#values = (2,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()

# run in terminal python my7testSelect.py : (1, 'Mary', 21)

# goto my7updateTable.py


##############################################################################
# this doesnt work#

# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="wsaa"
# )

# cursor = db.cursor()
# sql="select * from student where id = %s"
# values = (1,)

# cursor.execute(sql, values)
# result = cursor.fetchall()
# for x in result:
#   print(x)

# db.close()
# cursor.close()

