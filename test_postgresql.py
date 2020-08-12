# 
# in Postgresql db, create database:
'''
CREATE DATABASE suppliers;
'''

# in MacOS, remember to run: pip install psycopg2-binary
import psycopg2

def connect():
    return psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="pg123"
    )

def test_connection():
    conn = None

    try:
        conn = connect()
        cur = conn.cursor()
        print('Postgresql db version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        cur.close()
        print(db_version)

        return db_version
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


def create_tables():

    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        
        for command in commands:
            print('Running database command:\n' + command)
            cur.execute(command)
        
        # commit the changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_data():
    # executemany expects a sequence of sequences, eg. a list of lists/tuples
    vendor_list = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]
    sql = "insert into vendors(vendor_name) values(%s)"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.executemany(sql, vendor_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_part(part_name, vendor_list):
    """ add part data and assign vendor id with that part """

    sql_insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    sql_add_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    # In psycopg, the connection class is responsible for handling transactions. 
    # When the first SQL statement is issued to the PostgreSQL database using a 
    # cursor object, psycopg creates a new transaction. 
    # From that moment, psycopg executes all the subsequent statements in the same 
    # transaction. If any statement fails, psycopg will abort the transaction.

    # The connection class has two methods for terminating a transaction: commit() 
    # and rollback(). 
    # Closing the connection object or destroying it using the  del will also result
    # in an implicit rollback.

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql_insert_part, (part_name,))
        part_id = cur.fetchone()[0]
        for vendor_id in vendor_list:
            cur.execute(sql_add_vendor, (vendor_id, part_id))
        
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_parts():
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))





if __name__ == '__main__':
    # test_connection()
    # create_tables()
    # insert_data()
    insert_parts()
