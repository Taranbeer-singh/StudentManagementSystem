# Student Management System


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

        # Take student details from the user
        print("\n----- Add Student -----")

        name = input("Enter Student Name: ")
        roll_no = int(input("Enter Student Roll No.: "))
        course = input("Enter Student Course: ")
        age = int(input("Enter Student Age: "))
        marks = int(input("Enter Student Marks: "))


        # Create a dictionary to store one student's information
        student = {
            "name": name,
            "roll_no": roll_no,
            "course": course,
            "age": age,
            "marks": marks
        }


        # Add the student to the student list
        students.append(student)

        print("\nStudent added successfully!")


    # View Students
    elif choice == "2":

        print("\n----- Student List -----")

        # Check whether the student list is empty
        if len(students) == 0:
            print("No students found.")

        else:

            # Display details of all stored students
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

        # Take roll number to search
        search_roll_no = int(input("Enter Roll No. to search: "))

        # Initially assume that the student is not found
        found = False


        # Search through all students
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


        # Display message if student was not found
        if found == False:
            print("\nStudent not found.")


    # Update Student
    elif choice == "4":

        print("\n----- Update Student -----")

        # Take roll number of the student to update
        update_roll_no = int(input("Enter Roll No. to update: "))

        # Initially assume that the student is not found
        found = False


        # Search for the student
        for student in students:

            if student["roll_no"] == update_roll_no:

                print("\nStudent Found!")

                # Take new details from the user
                print("\nEnter New Details")

                student["name"] = input("Enter New Name: ")
                student["course"] = input("Enter New Course: ")
                student["age"] = int(input("Enter New Age: "))
                student["marks"] = int(input("Enter New Marks: "))

                print("\nStudent updated successfully!")

                found = True
                break


        # Display message if student was not found
        if found == False:
            print("\nStudent not found.")


    # Delete Student
    elif choice == "5":

        print("\n----- Delete Student -----")

        # Take roll number of the student to delete
        delete_roll_no = int(input("Enter Roll No. to delete: "))

        # Initially assume that the student is not found
        found = False


        # Search for the student
        for student in students:

            if student["roll_no"] == delete_roll_no:

                # Remove the student from the list
                students.remove(student)

                print("\nStudent deleted successfully!")

                found = True
                break


        # Display message if student was not found
        if found == False:
            print("\nStudent not found.")


    # Exit program
    elif choice == "6":

        print("\nExiting Student Management System...")
        break


    # Handle invalid menu choices
    else:

        print("\nInvalid choice!")