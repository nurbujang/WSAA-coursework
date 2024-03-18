import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="wsaa4"
)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)


cursor.execute(sql, values)

db.commit()
print("delete done")

db.close()
cursor.close()


# run in terminal 

# mysql:
# select * from student; joey deleted

# NEXT: HOW DO U PUT THESE INTO A DAO?
# GOTO my7zstudentDAO


###############################################################################

# import mysql.connector

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="wsaa"
# )

# cursor = db.cursor()
# sql="delete from student where id = %s"
# values = (2,)

# cursor.execute(sql, values)

# db.commit()
# print("delete done")

# db.close()
# cursor.close()