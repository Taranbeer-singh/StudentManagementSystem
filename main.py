# Student Management System


from validations import (
    get_valid_name,
    get_valid_roll_no,
    get_valid_course,
    get_valid_age,
    get_valid_marks
)


# Store all students in a list
students = []


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
    print("6. Exit")

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

        course = get_valid_course("Enter Student Course: ")

        age = get_valid_age("Enter Student Age: ")

        marks = get_valid_marks("Enter Student Marks: ")


        # Create dictionary for one student
        student = {
            "name": name,
            "roll_no": roll_no,
            "course": course,
            "age": age,
            "marks": marks
        }


        # Add student to list
        students.append(student)

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
                print("Age:", student["age"])
                print("Marks:", student["marks"])


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
                print("Age:", student["age"])
                print("Marks:", student["marks"])

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


                # Get validated new details
                name = get_valid_name("Enter New Name: ")

                course = get_valid_course("Enter New Course: ")

                age = get_valid_age("Enter New Age: ")

                marks = get_valid_marks("Enter New Marks: ")


                # Update student details
                student["name"] = name
                student["course"] = course
                student["age"] = age
                student["marks"] = marks


                print("\nStudent updated successfully!")

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

                print("\nStudent deleted successfully!")

                found = True
                break


        if found == False:
            print("\nStudent not found.")


    # Exit program
    elif choice == "6":

        print("\nExiting Student Management System...")
        break


    # Invalid menu choice
    else:

        print("\nInvalid choice!")