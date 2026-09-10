# SQLite Database Setup

import sqlite3


DATABASE_NAME = "students.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no INTEGER UNIQUE NOT NULL,
            course TEXT NOT NULL,
            year TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)


    # Student marks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            marks INTEGER NOT NULL,
            FOREIGN KEY (student_id)
                REFERENCES students(id)
        )
    """)


    connection.commit()

    connection.close()


create_database()
