import sqlite3 as sql

def db_env_create(table_name):
    # create sql lite 3 database
    conn = sql.connect('GOES_AWS_metadata.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF EXISTS '''+ table_name + ''' (
             filename VARCHAR NOT NULL, 
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
             link VARCHAR NOT NULL
             ); ''')
    return conn, cursor

def select_data(cursor, table_name):
    cursor.execute("SELECT * FROM "+table_name)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def db_conn_close(conn):
    conn.commit()
    print('Data entered successfully.')
    conn.close()
    if (conn):
        conn.close()
        print("The SQLite connection is closed.")
