# SQLite Database Functions

import sqlite3


DATABASE_NAME = "students.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def create_database():

    connection = get_connection()

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


def add_student(student):

    connection = get_connection()

    cursor = connection.cursor()


    # Add student information
    cursor.execute("""
        INSERT INTO students
        (name, roll_no, course, year, age)
        VALUES (?, ?, ?, ?, ?)
    """, (
        student["name"],
        student["roll_no"],
        student["course"],
        student["year"],
        student["age"]
    ))


    # Get ID of newly added student
    student_id = cursor.lastrowid


    # Add student's marks
    for subject, marks in student["marks"].items():

        cursor.execute("""
            INSERT INTO student_marks
            (student_id, subject, marks)
            VALUES (?, ?, ?)
        """, (
            student_id,
            subject,
            marks
        ))


    connection.commit()

    connection.close()


def get_all_students():

    connection = get_connection()

    cursor = connection.cursor()


    # Get all students
    cursor.execute("""
        SELECT id, name, roll_no, course, year, age
        FROM students
        ORDER BY id
    """)

    student_rows = cursor.fetchall()


    students = []


    # Get marks for each student
    for row in student_rows:

        student_id = row[0]

        cursor.execute("""
            SELECT subject, marks
            FROM student_marks
            WHERE student_id = ?
        """, (student_id,))

        mark_rows = cursor.fetchall()


        marks = {}

        for subject, mark in mark_rows:

            marks[subject] = mark


        student = {

            "name": row[1],

            "roll_no": row[2],

            "course": row[3],

            "year": row[4],

            "age": row[5],

            "marks": marks
        }


        students.append(student)


    connection.close()

    return students


def get_student_by_roll(roll_no):

    connection = get_connection()

    cursor = connection.cursor()


    # Find student by roll number
    cursor.execute("""
        SELECT id, name, roll_no, course, year, age
        FROM students
        WHERE roll_no = ?
    """, (roll_no,))

    row = cursor.fetchone()


    if row is None:

        connection.close()

        return None


    student_id = row[0]


    # Get student's marks
    cursor.execute("""
        SELECT subject, marks
        FROM student_marks
        WHERE student_id = ?
    """, (student_id,))

    mark_rows = cursor.fetchall()


    marks = {}

    for subject, mark in mark_rows:

        marks[subject] = mark


    student = {

        "name": row[1],

        "roll_no": row[2],

        "course": row[3],

        "year": row[4],

        "age": row[5],

        "marks": marks
    }


    connection.close()

    return student


def update_student(student):

    connection = get_connection()

    cursor = connection.cursor()


    # Find student ID using roll number
    cursor.execute("""
        SELECT id
        FROM students
        WHERE roll_no = ?
    """, (student["roll_no"],))

    row = cursor.fetchone()


    if row is None:

        connection.close()

        return False


    student_id = row[0]


    # Update student information
    cursor.execute("""
        UPDATE students
        SET name = ?,
            course = ?,
            year = ?,
            age = ?
        WHERE roll_no = ?
    """, (
        student["name"],
        student["course"],
        student["year"],
        student["age"],
        student["roll_no"]
    ))


    # Remove old marks
    cursor.execute("""
        DELETE FROM student_marks
        WHERE student_id = ?
    """, (student_id,))


    # Add new marks
    for subject, marks in student["marks"].items():

        cursor.execute("""
            INSERT INTO student_marks
            (student_id, subject, marks)
            VALUES (?, ?, ?)
        """, (
            student_id,
            subject,
            marks
        ))


    connection.commit()

    connection.close()

    return True


def delete_student(roll_no):

    connection = get_connection()

    cursor = connection.cursor()


    # Find student ID
    cursor.execute("""
        SELECT id
        FROM students
        WHERE roll_no = ?
    """, (roll_no,))

    row = cursor.fetchone()


    if row is None:

        connection.close()

        return False


    student_id = row[0]


    # Delete student's marks first
    cursor.execute("""
        DELETE FROM student_marks
        WHERE student_id = ?
    """, (student_id,))


    # Delete student
    cursor.execute("""
        DELETE FROM students
        WHERE roll_no = ?
    """, (roll_no,))


    connection.commit()

    connection.close()

    return True