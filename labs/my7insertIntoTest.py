import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="wsaa4"
)

cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)
#values = ("Joey",330)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()

# mysql:
# select * from student;

# goto my7testSelect.py


###################################################################################

# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="wsaa"
# )

# cursor = db.cursor()
# sql="insert into student (name, age) values (%s,%s)"
# values = ("Mary",21)

# cursor.execute(sql, values)

# db.commit()
# print("1 record inserted, ID:", cursor.lastrowid)

# db.close()
# cursor.close()