import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="test_db"
)

cursor = db.cursor()
# cursor.execute("CREATE TABLE salesman (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, "
#                "salesman_id INT,"
#                "name VARCHAR(255), "
#                "city VARCHAR(255),"
#                "commission FLOAT,"
#                "grade INT)")


# query = "INSERT INTO salesman (salesman_id, name, city, comission, grade) " \
#         "VALUES (%s, %s, %s, %s, %s)"
# values = [
#     (5001, "James Hoog", "New York", 0.15, 100),
#     (5002, "Nail Knite ", "Paris", 0.13, 200),
#     (5005, "Pit Alex", "London", 0.11, 150),
#     (5006, "Mc Lyon", "Paris", 0.14, 50),
#     (5007, "Paul Adam", "Rome ", 0.13, 200),
#     (5003, "Lauson Hen", "San Jose", 0.12, 300),
# ]
#
# cursor.executemany(query, values)
# db.commit()
# print(cursor.rowcount, "records inserted")
print('===== TASK 1 =====')
query = "SELECT * FROM salesman"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 2 =====')
query = "SELECT name, comission FROM salesman"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 3 =====')
query = "SELECT name FROM salesman WHERE comission > 0.13"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 4 =====')
query = "SELECT name FROM salesman WHERE city = 'Paris'"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 5 =====')
query = "SELECT * FROM salesman WHERE grade = 200"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 6 =====')
query = "SELECT name FROM salesman WHERE comission = (SELECT MAX(comission) FROM salesman)"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 6.1 =====')
query = "SELECT MAX(comission) FROM salesman"
cursor.execute(query)
print(cursor.fetchall())
print('===== TASK 7 =====')
query = "SELECT name FROM salesman WHERE comission = (SELECT MIN(comission) FROM salesman)"
cursor.execute(query)
print(cursor.fetchall())

db.close()