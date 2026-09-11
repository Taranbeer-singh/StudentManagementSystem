from database import create_database, add_student


# ==============================
# Create Database
# ==============================

create_database()


# ==============================
# Sample Students
# ==============================

students = [

    {
        "name": "Aarav Sharma",
        "roll_no": 101,
        "course": "BCA",
        "year": "1st Year",
        "age": 19,
        "marks": {
            "Programming in C": 78,
            "Mathematics": 72,
            "Computer Fundamentals": 85,
            "Communication Skills": 80
        }
    },

    {
        "name": "Aditi Verma",
        "roll_no": 102,
        "course": "BCA",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Python": 88,
            "DBMS": 81,
            "Data Structures": 76,
            "Computer Networks": 84
        }
    },

    {
        "name": "Ananya Singh",
        "roll_no": 103,
        "course": "BCA",
        "year": "3rd Year",
        "age": 21,
        "marks": {
            "Web Development": 91,
            "Software Engineering": 86,
            "Artificial Intelligence": 89,
            "Data Science": 93
        }
    },

    {
        "name": "Arjun Kumar",
        "roll_no": 104,
        "course": "BCA",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Python": 69,
            "DBMS": 74,
            "Data Structures": 71,
            "Computer Networks": 68
        }
    },

    {
        "name": "Harsh Mehta",
        "roll_no": 105,
        "course": "BCA",
        "year": "3rd Year",
        "age": 21,
        "marks": {
            "Web Development": 82,
            "Software Engineering": 79,
            "Artificial Intelligence": 75,
            "Data Science": 81
        }
    },

    {
        "name": "Simran Kaur",
        "roll_no": 106,
        "course": "BCA",
        "year": "1st Year",
        "age": 19,
        "marks": {
            "Programming in C": 86,
            "Mathematics": 79,
            "Computer Fundamentals": 91,
            "Communication Skills": 88
        }
    },

    {
        "name": "Bhavna Gupta",
        "roll_no": 107,
        "course": "BBA",
        "year": "1st Year",
        "age": 19,
        "marks": {
            "Accounting": 82,
            "Economics": 77,
            "Business Mathematics": 74,
            "Management": 85
        }
    },

    {
        "name": "Karan Malhotra",
        "roll_no": 108,
        "course": "BBA",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Marketing": 88,
            "Finance": 81,
            "Human Resource": 84,
            "Statistics": 79
        }
    },

    {
        "name": "Mehak Sharma",
        "roll_no": 109,
        "course": "BBA",
        "year": "3rd Year",
        "age": 21,
        "marks": {
            "Business Law": 76,
            "Entrepreneurship": 83,
            "Operations Management": 80,
            "Project Management": 87
        }
    },

    {
        "name": "Rohan Verma",
        "roll_no": 110,
        "course": "BBA",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Marketing": 71,
            "Finance": 68,
            "Human Resource": 75,
            "Statistics": 73
        }
    },

    {
        "name": "Yash Kapoor",
        "roll_no": 111,
        "course": "BBA",
        "year": "3rd Year",
        "age": 21,
        "marks": {
            "Business Law": 90,
            "Entrepreneurship": 86,
            "Operations Management": 88,
            "Project Management": 92
        }
    },

    {
        "name": "Aditya Raj",
        "roll_no": 112,
        "course": "B.Tech CSE",
        "year": "1st Year",
        "age": 19,
        "marks": {
            "Programming": 81,
            "Mathematics": 76,
            "Physics": 72,
            "Engineering Fundamentals": 85
        }
    },

    {
        "name": "Isha Patel",
        "roll_no": 113,
        "course": "B.Tech CSE",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Data Structures": 89,
            "DBMS": 85,
            "Operating Systems": 82,
            "Computer Networks": 88
        }
    },

    {
        "name": "Nikhil Sharma",
        "roll_no": 114,
        "course": "B.Tech CSE",
        "year": "3rd Year",
        "age": 21,
        "marks": {
            "Algorithms": 78,
            "Software Engineering": 84,
            "Artificial Intelligence": 87,
            "Web Development": 80
        }
    },

    {
        "name": "Priya Saini",
        "roll_no": 115,
        "course": "B.Tech CSE",
        "year": "4th Year",
        "age": 22,
        "marks": {
            "Machine Learning": 92,
            "Cloud Computing": 88,
            "Cyber Security": 94,
            "Project": 91
        }
    },

    {
        "name": "Rohit Kumar",
        "roll_no": 116,
        "course": "B.Tech CSE",
        "year": "2nd Year",
        "age": 20,
        "marks": {
            "Data Structures": 67,
            "DBMS": 73,
            "Operating Systems": 69,
            "Computer Networks": 71
        }
    },

    {
        "name": "Anmol Singh",
        "roll_no": 117,
        "course": "MCA",
        "year": "1st Year",
        "age": 22,
        "marks": {
            "Python": 84,
            "DBMS": 79,
            "Data Structures": 87,
            "Computer Networks": 82
        }
    },

    {
        "name": "Deepak Yadav",
        "roll_no": 118,
        "course": "MCA",
        "year": "1st Year",
        "age": 23,
        "marks": {
            "Python": 72,
            "DBMS": 68,
            "Data Structures": 75,
            "Computer Networks": 70
        }
    },

    {
        "name": "Neha Kapoor",
        "roll_no": 119,
        "course": "MCA",
        "year": "2nd Year",
        "age": 23,
        "marks": {
            "Machine Learning": 91,
            "Cloud Computing": 86,
            "Artificial Intelligence": 89,
            "Project": 94
        }
    },

    {
        "name": "Varun Sharma",
        "roll_no": 120,
        "course": "MCA",
        "year": "2nd Year",
        "age": 24,
        "marks": {
            "Machine Learning": 78,
            "Cloud Computing": 81,
            "Artificial Intelligence": 76,
            "Project": 85
        }
    }
]


# ==============================
# Add Students to Database
# ==============================

for student in students:

    add_student(student)


print("20 sample students added successfully.")