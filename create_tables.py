import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the songdb
    - Returns the connection and cursor to songdb
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=user")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create song database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS songdb")
    cur.execute("CREATE DATABASE songdb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to songdb database
    conn = psycopg2.connect("host=127.0.0.1 dbname=songdb user=postgres password=user")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the songdb database.
    
    - Establishes connection with the songdb  database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    #drop_tables(cur, conn) # firstime creating your databese don't use this code
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()