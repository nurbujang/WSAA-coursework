import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="wsaa4"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s  where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()

# run in terminal python my7testSelect.py : (1, 'Joe', 33)

# mysql:
# select * from student; (now joe is in position 1)

# goto my7xdeleteRow.py


###############################################################################

# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#  database="wsaa"
# )

# cursor = db.cursor()
# sql="update student set name= %s, age=%s  where id = %s"
# values = ("Joe",33, 1)

# cursor.execute(sql, values)

# db.commit()
# print("update done")

# cursor.close()
# db.close()
