import mysql.connector as mysql


def created_orders(ord_no, purch_amt, ord_date, customer_id, salesman_id):
    return f"INSERT INTO orders(ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUE ({ord_no}, {purch_amt}, {ord_date}, {customer_id}, {salesman_id});"


try:
    db = mysql.connect(host="localhost",
                       user="root",
                       passwd="Mywill11",
                       database="hw_mysql")

    try:
        cursor = db.cursor()
        # create_table = "CREATE TABLE orders(ord_no int not null primary key, purch_amt float not null, ord_date varchar(32) not null, customer_id int not null, salesman_id int not null);"
        # cursor.execute(create_table)
        # print("Table created")
        # oreder_70013 = created_orders(70013, 3045.6, '2012-04-25', 3002, 5001)
        # cursor.execute(oreder_70013)
        # db.commit()
        select_all = 'SELECT * FROM orders'
        # cursor.execute(select_all)
        # ---------- FIRST TASK -------------------
        select_first_task = 'SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id LIKE 5002'
        cursor.execute(select_first_task)
        rows_1 = cursor.fetchall()
        for row in rows_1:
            print(row)
        print("FIRST TASK")
        print("*" * 20)
        # -----------------------------------------
        # ---------- SECOND TASK -------------------
        select_second_task = 'SELECT DISTINCT salesman_id FROM orders'
        cursor.execute(select_second_task)
        rows_2 = cursor.fetchall()
        for row in rows_2:
            print(row)
        print("SECOND TASK")
        print("*" * 20)
        # -----------------------------------------
        # ---------- THIRD TASK -------------------
        select_third_task = 'SELECT DISTINCT salesman_id FROM orders'
        cursor.execute(select_third_task)
        rows_3 = cursor.fetchall()
        for row in rows_3:
            print(row)
        print("THIRD TASK")
        print("*" * 20)
        # -----------------------------------------
        # ---------- FOURTH TASK -------------------
        select_fourth_task = 'SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders ORDER BY ord_date'
        cursor.execute(select_fourth_task)
        rows_4 = cursor.fetchall()
        for row in rows_4:
            print(row)
        print("FOURTH TASK")
        print("*" * 20)
        # -----------------------------------------
        # ---------- FIFTH TASK -------------------
        select_fifth_task = 'SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007'
        cursor.execute(select_fifth_task)
        rows_5 = cursor.fetchall()
        for row in rows_5:
            print(row)
        print("FIFTH TASK")
        print("*" * 20)
        # -----------------------------------------
    finally:
        db.close()

except Exception as ex:
    print(ex)
