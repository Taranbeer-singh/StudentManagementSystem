# Student Management System

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


# Load existing students from file
students = load_students()


while True:

    # Display main menu
    print("\n========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")

    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    # Add Student
    if choice == "1":

        print("\n----- Add Student -----")

        # Get validated student details
        name = get_valid_name("Enter Student Name: ")

        roll_no = get_valid_roll_no(
            "Enter Student Roll No.: ",
            students
        )


        # Select Course
        print("\nAvailable Courses:")

        course_list = list(courses.keys())

        for index, course in enumerate(course_list, start=1):
            print(f"{index}. {course}")


        while True:

            try:

                course_choice = int(
                    input("\nSelect Course: ")
                )

                if course_choice < 1 or course_choice > len(course_list):
                    print("Invalid course choice.")
                    continue

                course = course_list[course_choice - 1]

                break

            except ValueError:

                print("Invalid input! Please enter a number.")


        # Select Year
        print(f"\nAvailable Years for {course}:")

        year_list = list(courses[course].keys())

        for index, year in enumerate(year_list, start=1):
            print(f"{index}. {year}")


        while True:

            try:

                year_choice = int(
                    input("\nSelect Year: ")
                )

                if year_choice < 1 or year_choice > len(year_list):
                    print("Invalid year choice.")
                    continue

                year = year_list[year_choice - 1]

                break

            except ValueError:

                print("Invalid input! Please enter a number.")


        # Get subjects for selected course and year
        subjects = courses[course][year]


        print("\nEnter Marks:")

        marks = {}


        # Get marks for each subject
        for subject in subjects:

            marks[subject] = get_valid_marks(
                f"Enter marks for {subject}: "
            )


        # Get age
        age = get_valid_age("Enter Student Age: ")


        # Create dictionary for one student
        student = {

            "name": name,

            "roll_no": roll_no,

            "course": course,

            "year": year,

            "age": age,

            "marks": marks
        }


        # Add student to list
        students.append(student)


        # Save updated list to file
        save_students(students)


        print("\nStudent added successfully!")


    # View Students
    elif choice == "2":

        print("\n----- Student List -----")


        if len(students) == 0:

            print("No students found.")


        else:

            for student in students:

                print("\n-------------------------")

                print("Name:", student["name"])

                print("Roll No.:", student["roll_no"])

                print("Course:", student["course"])

                print("Year:", student["year"])

                print("Age:", student["age"])


                print("Marks:")

                for subject, marks in student["marks"].items():

                    print(
                        f"  {subject}: {marks}/100"
                    )


                # Calculate total and percentage
                (
                    total_marks,
                    obtained_marks,
                    percentage
                ) = get_student_marks_statistics(student)


                print(
                    "\nTotal Marks:",
                    f"{obtained_marks}/{total_marks}"
                )

                print(
                    "Percentage:",
                    f"{percentage:.2f}%"
                )


    # Search Student
    elif choice == "3":

        print("\n----- Search Student -----")


        search_roll_no = get_valid_roll_no(
            "Enter Roll No. to search: "
        )


        found = False


        for student in students:

            if student["roll_no"] == search_roll_no:

                print("\nStudent Found!")

                print("Name:", student["name"])

                print("Roll No.:", student["roll_no"])

                print("Course:", student["course"])

                print("Year:", student["year"])

                print("Age:", student["age"])


                print("Marks:")

                for subject, marks in student["marks"].items():

                    print(
                        f"  {subject}: {marks}/100"
                    )


                # Calculate total and percentage
                (
                    total_marks,
                    obtained_marks,
                    percentage
                ) = get_student_marks_statistics(student)


                print(
                    "\nTotal Marks:",
                    f"{obtained_marks}/{total_marks}"
                )

                print(
                    "Percentage:",
                    f"{percentage:.2f}%"
                )


                found = True

                break


        if found == False:

            print("\nStudent not found.")


    # Update Student
    elif choice == "4":

        print("\n----- Update Student -----")


        update_roll_no = get_valid_roll_no(
            "Enter Roll No. to update: "
        )


        found = False


        for student in students:

            if student["roll_no"] == update_roll_no:

                print("\nStudent Found!")

                print("\nEnter New Details")


                # Get new name
                name = get_valid_name(
                    "Enter New Name: "
                )


                # Get new age
                age = get_valid_age(
                    "Enter New Age: "
                )


                # Select new course
                print("\nAvailable Courses:")

                course_list = list(courses.keys())


                for index, course in enumerate(
                    course_list,
                    start=1
                ):

                    print(f"{index}. {course}")


                while True:

                    try:

                        course_choice = int(
                            input("\nSelect Course: ")
                        )


                        if (
                            course_choice < 1
                            or course_choice > len(course_list)
                        ):

                            print("Invalid course choice.")

                            continue


                        course = course_list[
                            course_choice - 1
                        ]

                        break


                    except ValueError:

                        print(
                            "Invalid input! "
                            "Please enter a number."
                        )


                # Select new year
                print(
                    f"\nAvailable Years for {course}:"
                )


                year_list = list(
                    courses[course].keys()
                )


                for index, year in enumerate(
                    year_list,
                    start=1
                ):

                    print(f"{index}. {year}")


                while True:

                    try:

                        year_choice = int(
                            input("\nSelect Year: ")
                        )


                        if (
                            year_choice < 1
                            or year_choice > len(year_list)
                        ):

                            print("Invalid year choice.")

                            continue


                        year = year_list[
                            year_choice - 1
                        ]

                        break


                    except ValueError:

                        print(
                            "Invalid input! "
                            "Please enter a number."
                        )


                # Get subjects for new course and year
                subjects = courses[course][year]


                print("\nEnter New Marks:")


                marks = {}


                for subject in subjects:

                    marks[subject] = get_valid_marks(
                        f"Enter marks for {subject}: "
                    )


                # Update student details
                student["name"] = name

                student["course"] = course

                student["year"] = year

                student["age"] = age

                student["marks"] = marks


                # Save updated list to file
                save_students(students)


                print(
                    "\nStudent updated successfully!"
                )


                found = True

                break


        if found == False:

            print("\nStudent not found.")


    # Delete Student
    elif choice == "5":

        print("\n----- Delete Student -----")


        delete_roll_no = get_valid_roll_no(
            "Enter Roll No. to delete: "
        )


        found = False


        for student in students:

            if student["roll_no"] == delete_roll_no:

                students.remove(student)


                # Save updated list to file
                save_students(students)


                print(
                    "\nStudent deleted successfully!"
                )


                found = True

                break


        if found == False:

            print("\nStudent not found.")


    # Statistics
    elif choice == "6":

        print("\n----- Student Statistics -----")


        if len(students) == 0:

            print("\nNo students found.")

        else:

            # Overall statistics
            (
                total_students,
                average_marks,
                highest_marks,
                lowest_marks
            ) = get_overall_statistics(students)


            print(
                "\nTotal Students:",
                total_students
            )

            print(
                "Average Percentage:",
                f"{average_marks:.2f}%"
            )

            print(
                "Highest Marks:",
                highest_marks
            )

            print(
                "Lowest Marks:",
                lowest_marks
            )


            # Course-wise statistics
            course_statistics = get_course_statistics(
                students
            )


            print("\nCourse-wise Students:")


            for course, count in course_statistics.items():

                print(
                    f"{course}: {count}"
                )


            # Year-wise statistics
            year_statistics = get_year_statistics(
                students
            )


            print("\nYear-wise Students:")


            for year, count in year_statistics.items():

                print(
                    f"{year}: {count}"
                )


            # Subject-wise average marks
            subject_statistics = get_subject_statistics(
                students
            )


            print("\nSubject-wise Average Marks:")


            for subject, average in subject_statistics.items():

                print(
                    f"{subject}: {average:.2f}"
                )


    # Exit program
    elif choice == "7":

        print(
            "\nExiting Student Management System..."
        )

        break


    # Invalid menu choice
    else:

        print("\nInvalid choice!")