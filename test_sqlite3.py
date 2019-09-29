
import sqlite3
from sqlite3 import Error


def sql_conn():
    try:
        # A new file called 'test_sqlite3.db' will be created
        con = sqlite3.connect('test_sqlite3.db')
        return con
    except Error as e:
        print(e)


def sql_cr_table(con):
    cursorObj = con.cursor()  # get cursor object from connection
    cursorObj.execute("""CREATE TABLE IF NOT EXISTS employees(
        id integer PRIMARY KEY, 
        name text, 
        salary real, 
        department text, 
        position text, 
        hireDate text
    )""")
    con.commit()

def sql_inst_rows(con):
    cur = con.cursor()
    cur.execute("DELETE FROM employees")

    # literal insert
    cur.execute("""INSERT INTO employees
        VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')
    """)

    # single row inseret
    data = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
    cur.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) 
        VALUES(?, ?, ?, ?, ?, ?)''', data
    )

    # multiple rows insert
    data_list = [
        (3, 'Amy', 600, 'IT', 'Tech', '2018-03-20'),
        (4, 'Kevin', 750, 'IT', 'Tech', '2017-01-05')
    ]
    cur.executemany('''INSERT INTO employees(id, name, salary, department, position, hireDate)
        VALUES(?, ?, ?, ?, ?, ?)''', data_list
    )

    con.commit()


def sql_rows(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    return rows

def sql_drp_table(con):
    con.cursor().execute('DROP TABLE IF EXISTS employees')
    con.commit()


# use with to always auto close connection
with sql_conn() as conn: 
    conn = sql_conn()
    sql_cr_table(conn)
    sql_inst_rows(conn)

    for r in sql_rows(conn):
        print(r)

    # sql_drp_table(conn)







