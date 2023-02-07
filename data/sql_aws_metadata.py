import sqlite3 as sql

def create_database():
    conn = sql.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor

def create_table_goes(cursor, table_name):
    # create sql lite 3 database
    cursor.execute(''' CREATE TABLE IF EXISTS '''+ table_name + ''' (
             year INTEGER NOT NULL,
             day INTEGER NOT NULL,
             hour INTEGER NOT NULL
             ); ''')

def create_table_nexrad(cursor, table_name):
    # create sql lite 3 database
    cursor.execute(''' CREATE TABLE IF EXISTS '''+ table_name + ''' (
             station_id INTEGER NOT NULL,
             year INTEGER NOT NULL,
             day INTEGER NOT NULL,
             hour INTEGER NOT NULL
             ); ''')


def print_and_validate_data(cursor, table_name):
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

database_name = 'metadata_storage'
table_name_goes = 'goes_metadata'
table_name_nexrad = 'goes_metadata'
conn, cursor = create_database(table_name_goes)
create_table_goes(conn, cursor, table_name_goes)
create_table_nexrad(conn, cursor, table_name_nexrad)
db_conn_close(conn)