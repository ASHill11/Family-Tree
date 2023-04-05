import os
import sqlite3
from person_init import * # all functions relating to the Person object

def create_person_table(conn):
    if conn is not None:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS person (
        id integer PRIMARY KEY,
        fname text,
        lname text,
        class_year integer,
        parents text,
        children text
        );
        """)
    else:
        print("Error: database connection does not exist.")

def create_connection():
    # creates a database connection to a SQLite database or creates a new database if it doesn't exist
    try:
        conn = sqlite3.connect(os.getcwd() + '/sqlite3-db/pythonsqlite.db')
        create_person_table(conn)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def add_people_to_db(conn, people):
    if conn is not None:
        c = conn.cursor()
        for person in people:
            insert_command = (f"INSERT OR REPLACE INTO person VALUES ({person.parse_id}, \"{person.first_name}\", \"{person.last_name}\", {person.class_year}, \"{' '.join(map(str, person.parents))}\", \"{' '.join(map(str, person.children))}\");")
            c.execute(insert_command)
        conn.commit()
    else:
        print("Error: database connection does not exist.")

def clear_db_people():
    conn = create_connection()
    if conn is not None:
        c = conn.cursor()
        c.execute("DROP TABLE person;")
        conn.commit()
        conn.close()
    else:
        print("Error: database connection does not exist.")

def get_people_from_db(conn):
    people = []
    if conn is not None:
        c = conn.cursor()
        c.execute("SELECT * FROM person;")
        person_table = c.fetchall()
        for person_info in person_table:
            parse_id, first_name, last_name, class_year, parents_str, children_str = person_info
            parents = list(map(int, str(parents_str).split()))
            children = list(map(int, str(children_str).split()))
            person = Person(first_name, last_name, class_year, parse_id, parents, children)
            people.append(person)
    else:
        print("Error: database connection does not exist.")
    return people