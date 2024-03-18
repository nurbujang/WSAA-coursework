import mysql.connector
class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self):
#these should be read from a config file
            self.host="127.0.0.1"
            self.user="root"
            self.password="root"
            self.database="wsaa4"

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
    )   
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        for row in result:
            studentlist.append(self.convertToDict(row))

        self.closeAll()
        return studentlist
         
    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result) 
         
    def update(self, values):
        cursor = self.getCursor()
        sql="update student set name= %s, age=%s  where id = %s"
    
        values = (values.get("name"), values.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return values

         
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")
        return True

# make a utility function
    def convertToDict(self,resultLine):
        studentKeys = ["id", "name", "age"]
        currentkey = 0
        student = {}
        for attrib in resultLine:
            student[studentKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return student

# your code here
studentDAO = StudentDAO()