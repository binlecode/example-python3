
import test_postgresql as tpg

# make sure stored procedures are compiled in `suppliers` db:
'''
CREATE OR REPLACE PROCEDURE add_new_part(
	new_part_name varchar,
	new_vendor_name varchar
) 
AS $$
DECLARE
	v_part_id INT;
	v_vendor_id INT;
BEGIN
	-- insert into the parts table
	INSERT INTO parts(part_name) 
	VALUES(new_part_name) 
	RETURNING part_id INTO v_part_id;
	
	-- insert a new vendor
	INSERT INTO vendors(vendor_name)
	VALUES(new_vendor_name)
	RETURNING vendor_id INTO v_vendor_id;
	
	-- insert into vendor_parts
	INSERT INTO vendor_parts(part_id, vendor_id)
	VALUEs(v_part_id, v_vendor_id);
	
END;
$$
LANGUAGE PLPGSQL;
'''

def add_new_parts():

    # Starting from psycopg 2.5, the connection and cursor are Context Managers
    # and therefore you can use them with the with statement.
    # Psycopg commits the transaction if no exception occurs within the with block, 
    # and otherwise it rolls back the transaction.
    with tpg.connect() as conn:
        with conn.cursor() as cur:
            cur.execute('CALL add_new_part(%s, %s)', ('OLED', 'LG'))
    
    # Unlike other context manager objects, existing the with block does not close 
    # the connection but only terminates the transaction. 
    # As the result, you can use the same connection object in the subsequent with 
    # statement in another transaction as follows:
    conn = None
    try:
        conn = tpg.connect()
        # transaction 1
        with conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_part(%s, %s)', ('Toilet', 'Toto'))

        # transaction 2
        with conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_part(%s, %s)', ('Thinkpad', 'Lenovo'))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    add_new_parts()