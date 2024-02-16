import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='demodb'
)

cursorObject = mydb.cursor()
# cursorObject.execute("SHOW DATABASES")

studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""

# table created
# cursorObject.execute(studentRecord)

# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = [("Nikhil", "CSE", "98", "A", "18"),
#        ("Nisha", "CSE", "99", "A", "18"),
#        ("Rohan", "MAE", "43", "B", "20"),
#        ("Amit", "ECE", "24", "A", "21"),
#        ("Anil", "MAE", "45", "B", "20"),
#        ("Megha", "ECE", "55", "A", "22"),
#        ("Sita", "CSE", "95", "A", "19")]
# cursorObject.executemany(sql, val)

# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = ("Ram", "CSE", "85", "B", "19")
# cursorObject.execute(sql,val)
# mydb.commit()

query = "SELECT NAME, ROLL FROM STUDENT where section ='A'"
cursorObject.execute(query)
myresult = cursorObject.fetchall()
for x in myresult:
    print(x)

mydb.close()
