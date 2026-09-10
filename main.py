from validations import (
    get_valid_name,
    get_valid_roll_no,
    get_valid_age,
    get_valid_marks
)

from file_handler import save_students, load_students

from courses import courses

from statistics import (
    get_overall_statistics,
    get_course_statistics,
    get_year_statistics,
    get_student_marks_statistics,
    get_subject_statistics
)

from database import (
    create_database,
    add_student,
    get_all_students,
    get_student_by_roll,
    update_student,
    delete_student
)


# Create SQLite database and tables
create_database()

# Load students from SQLite
students = get_all_students()


while True:

    print("\n========== Student Management System ==========")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    # ==============================
    # Add Student
    # ==============================

    if choice == "1":

        print("\n----- Add Student -----")

        name = get_valid_name("Enter Student Name: ")

        roll_no = get_valid_roll_no(
            "Enter Roll No.: ",
            students
        )

        print("\nAvailable Courses:")

        course_list = list(courses.keys())

        for index, course_name in enumerate(course_list, start=1):

            print(f"{index}. {course_name}")


        while True:

            try:

                course_choice = int(
                    input("Select Course: ")
                )

                if 1 <= course_choice <= len(course_list):
                    course = course_list[course_choice - 1]
                    break

                print("Invalid course selection.")

            except ValueError:

                print("Please enter a valid number.")


        print("\nAvailable Years:")

        year_list = list(courses[course].keys())

        for index, year_name in enumerate(year_list, start=1):

            print(f"{index}. {year_name}")


        while True:

            try:

                year_choice = int(
                    input("Select Year: ")
                )

                if 1 <= year_choice <= len(year_list):
                    year = year_list[year_choice - 1]
                    break

                print("Invalid year selection.")

            except ValueError:

                print("Please enter a valid number.")


        age = get_valid_age("Enter Age: ")


        print("\nEnter Marks:")

        subjects = courses[course][year]

        marks = {}


        for subject in subjects:

            marks[subject] = get_valid_marks(
                f"Enter marks for {subject}: "
            )


        student = {

            "name": name,
            "roll_no": roll_no,
            "course": course,
            "year": year,
            "age": age,
            "marks": marks
        }


        # Save student to SQLite
        add_student(student)

        # Refresh students list
        students = get_all_students()

        print("\nStudent added successfully!")


    # ==============================
    # View Students
    # ==============================

    elif choice == "2":

        print("\n----- Student List -----")


        if len(students) == 0:

            print("No students found.")

        else:

            for student in students:

                print("\n------------------------")

                print("Name:", student["name"])
                print("Roll No.:", student["roll_no"])
                print("Course:", student["course"])
                print("Year:", student["year"])
                print("Age:", student["age"])

                print("Marks:")

                for subject, marks in student["marks"].items():

                    print(f"{subject}: {marks}")

                total_marks = sum(
                    student["marks"].values()
                )

                maximum_marks = len(
                    student["marks"]
                ) * 100

                percentage = (
                    total_marks / maximum_marks
                ) * 100

                print("Total Marks:", total_marks)
                print("Percentage:", f"{percentage:.2f}%")


    # ==============================
    # Search Student
    # ==============================

    elif choice == "3":

        print("\n----- Search Student -----")


        search_roll_no = get_valid_roll_no(
            "Enter Roll No. to search: "
        )


        student = get_student_by_roll(
            search_roll_no
        )


        if student is not None:

            print("\nStudent Found!")

            print("\nName:", student["name"])
            print("Roll No.:", student["roll_no"])
            print("Course:", student["course"])
            print("Year:", student["year"])
            print("Age:", student["age"])

            print("\nMarks:")

            for subject, marks in student["marks"].items():

                print(f"{subject}: {marks}")


            total_marks = sum(
                student["marks"].values()
            )

            maximum_marks = len(
                student["marks"]
            ) * 100

            percentage = (
                total_marks / maximum_marks
            ) * 100


            print("\nTotal Marks:", total_marks)
            print(
                "Percentage:",
                f"{percentage:.2f}%"
            )

        else:

            print("\nStudent not found.")


    # ==============================
    # Update Student
    # ==============================

    elif choice == "4":

        print("\n----- Update Student -----")


        update_roll_no = get_valid_roll_no(
            "Enter Roll No. to update: "
        )


        # Find student directly from SQLite
        existing_student = get_student_by_roll(
            update_roll_no
        )


        if existing_student is None:

            print("\nStudent not found.")

        else:

            print("\nStudent Found!")

            print(
                "Current Name:",
                existing_student["name"]
            )

            print(
                "Current Course:",
                existing_student["course"]
            )

            print(
                "Current Year:",
                existing_student["year"]
            )

            print(
                "Current Age:",
                existing_student["age"]
            )


            print("\nEnter New Details:")


            name = get_valid_name(
                "Enter New Student Name: "
            )


            print("\nAvailable Courses:")

            course_list = list(courses.keys())


            for index, course_name in enumerate(
                course_list,
                start=1
            ):

                print(
                    f"{index}. {course_name}"
                )


            while True:

                try:

                    course_choice = int(
                        input("Select New Course: ")
                    )


                    if 1 <= course_choice <= len(course_list):

                        course = course_list[
                            course_choice - 1
                        ]

                        break


                    print("Invalid course selection.")


                except ValueError:

                    print(
                        "Please enter a valid number."
                    )


            print("\nAvailable Years:")

            year_list = list(
                courses[course].keys()
            )


            for index, year_name in enumerate(
                year_list,
                start=1
            ):

                print(
                    f"{index}. {year_name}"
                )


            while True:

                try:

                    year_choice = int(
                        input("Select New Year: ")
                    )


                    if 1 <= year_choice <= len(year_list):

                        year = year_list[
                            year_choice - 1
                        ]

                        break


                    print("Invalid year selection.")


                except ValueError:

                    print(
                        "Please enter a valid number."
                    )


            age = get_valid_age(
                "Enter New Age: "
            )


            print("\nEnter New Marks:")

            subjects = courses[course][year]

            marks = {}


            for subject in subjects:

                marks[subject] = get_valid_marks(
                    f"Enter marks for {subject}: "
                )


            updated_student = {

                "name": name,

                # Roll number remains unchanged
                "roll_no": update_roll_no,

                "course": course,

                "year": year,

                "age": age,

                "marks": marks
            }


            # Update student in SQLite
            update_student(
                updated_student
            )


            # Refresh students list
            students = get_all_students()


            print(
                "\nStudent updated successfully!"
            )


    # ==============================
    # Delete Student
    # ==============================

    elif choice == "5":

        print("\n----- Delete Student -----")


        delete_roll_no = get_valid_roll_no(
            "Enter Roll No. to delete: "
        )


        # Delete student directly from SQLite
        deleted = delete_student(
            delete_roll_no
        )


        if deleted:

            # Refresh students list
            students = get_all_students()

            print(
                "\nStudent deleted successfully!"
            )

        else:

            print("\nStudent not found.")


    # ==============================
    # Student Statistics
    # ==============================

    elif choice == "6":

        print("\n----- Student Statistics -----")

        total_students, average_marks, highest_marks, lowest_marks = (
            get_overall_statistics(students)
        )


        print(
            "\nTotal Students:",
            total_students
        )

        print(
            "Average Marks:",
            f"{average_marks:.2f}"
        )

        print(
            "Highest Marks:",
            highest_marks
        )

        print(
            "Lowest Marks:",
            lowest_marks
        )


        print("\n----- Course Statistics -----")

        course_statistics = get_course_statistics(
            students
        )


        for course, count in course_statistics.items():

            print(
                f"{course}: {count} student(s)"
            )


        print("\n----- Year Statistics -----")

        year_statistics = get_year_statistics(
            students
        )


        for year, count in year_statistics.items():

            print(
                f"{year}: {count} student(s)"
            )


        print("\n----- Subject Average Statistics -----")

        subject_statistics = get_subject_statistics(
            students
        )


        for subject, average in subject_statistics.items():

            print(
                f"{subject}: {average:.2f}"
            )


    # ==============================
    # Exit
    # ==============================

    elif choice == "7":

        print(
            "\nThank you for using Student Management System!"
        )

        break


    else:

        print("\nInvalid choice! Please try again.")