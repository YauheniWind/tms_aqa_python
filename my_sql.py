import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="Mywill11",
                   database="test_db_3")

cursor = db.cursor()


# cursor.execute("CREATE DATABASE test_db_3")
# table = cursor.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null)")

sql = "insert into Employee(name, id, salary, dept_id) values(%s, %s, %s, %s)"

val = ("John", 110, 25000.00, 201)
cursor.execute(sql, val)
db.commit()
cursor.execute("DESC employee")
# cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
