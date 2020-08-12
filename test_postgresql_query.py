
import test_postgresql as tpg


conn = tpg.connect()

with conn: 
    with conn.cursor() as cur:

        # The  fetchone() fetches the next row in the result set. 
        # It returns a single tuple or None when no more row is available.
        cur.execute('select * from parts where part_name = %s', ('Thinkpad',))
        print('show one part:')
        rs = cur.fetchone()
        print(rs)
        print('type of resultset: ', type(rs))
        print('cursor description: ', cur.description)

    with conn.cursor() as cur:
        # The  fetchmany(size=cursor.arraysize) fetches the next set of rows 
        # specified by the size parameter. 
        # If size is omitted, the  arraysize will determine the number of rows 
        # to be fetched. 
        # The  fetchmany() method returns a list of tuples or an empty list if 
        # no more rows available.

        cur.execute('select * from vendors limit 10')
        print('list 5 vendors:')
        for r in cur.fetchmany(5):
            print(r)

        # fetchall will fetch the remainder of the same resultset (finishing the cursor)
        # fetchall returns a list of tuples, empty list if there's no rows to fetch
        print('list the rest of vendors from result set')
        for r in cur.fetchall():
            print(r)
        # try fetchall again will return an empty list
        if not cur.fetchall():
            print('empty resultset: cursor reached bottom')


    # using extra module for add-on features
    import psycopg2.extras

    # following query shows two things:
    # - dict-like item from the cursor iteration supported by extra module
    # - cursor itself is iterable that can be called directly in for .. in
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute('select * from vendors limit 3')
        
        print('showing a few vendors:')
        for c in cur:
            print('vendor_id=', c['vendor_id'], ', vendor_name=', c['vendor_name'])
            
