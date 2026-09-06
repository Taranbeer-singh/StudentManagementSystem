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

        print("\n----- Add Student -----")


        # Validate student name
        while True:

            name = input("Enter Student Name: ")

            # Check whether name is empty
            if name.strip() == "":
                print("Name cannot be empty.")
                continue

            # Check whether name contains only letters and spaces
            if not name.replace(" ", "").isalpha():
                print("Name can contain only letters and spaces.")
                continue

            break


        # Validate student roll number
        while True:

            try:
                roll_no = int(input("Enter Student Roll No.: "))

                # Roll number must be positive
                if roll_no <= 0:
                    print("Roll No. must be greater than 0.")
                    continue

                # Check duplicate roll number
                duplicate = False

                for student in students:

                    if student["roll_no"] == roll_no:
                        duplicate = True
                        break

                if duplicate:
                    print("Roll No. already exists.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


        # Validate student course
        while True:

            course = input("Enter Student Course: ")

            # Course cannot be empty
            if course.strip() == "":
                print("Course cannot be empty.")
                continue

            break


        # Validate student age
        while True:

            try:
                age = int(input("Enter Student Age: "))

                # Age must be greater than 0
                if age <= 0:
                    print("Age must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


        # Validate student marks
        while True:

            try:
                marks = int(input("Enter Student Marks: "))

                # Marks must be between 0 and 100
                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


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


        # Check whether list is empty
        if len(students) == 0:
            print("No students found.")

        else:

            # Display all students
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


        # Validate search roll number
        while True:

            try:
                search_roll_no = int(input("Enter Roll No. to search: "))

                if search_roll_no <= 0:
                    print("Roll No. must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


        # Initially assume student is not found
        found = False


        # Search through students
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


        # Validate update roll number
        while True:

            try:
                update_roll_no = int(input("Enter Roll No. to update: "))

                if update_roll_no <= 0:
                    print("Roll No. must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


        # Initially assume student is not found
        found = False


        # Search for student
        for student in students:

            if student["roll_no"] == update_roll_no:

                print("\nStudent Found!")
                print("\nEnter New Details")


                # Validate new name
                while True:

                    name = input("Enter New Name: ")

                    if name.strip() == "":
                        print("Name cannot be empty.")
                        continue

                    if not name.replace(" ", "").isalpha():
                        print("Name can contain only letters and spaces.")
                        continue

                    break


                # Validate new course
                while True:

                    course = input("Enter New Course: ")

                    if course.strip() == "":
                        print("Course cannot be empty.")
                        continue

                    break


                # Validate new age
                while True:

                    try:
                        age = int(input("Enter New Age: "))

                        if age <= 0:
                            print("Age must be greater than 0.")
                            continue

                        break

                    except ValueError:
                        print("Invalid input! Please enter a number.")


                # Validate new marks
                while True:

                    try:
                        marks = int(input("Enter New Marks: "))

                        if marks < 0 or marks > 100:
                            print("Marks must be between 0 and 100.")
                            continue

                        break

                    except ValueError:
                        print("Invalid input! Please enter a number.")


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


        # Validate delete roll number
        while True:

            try:
                delete_roll_no = int(input("Enter Roll No. to delete: "))

                if delete_roll_no <= 0:
                    print("Roll No. must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter a number.")


        # Initially assume student is not found
        found = False


        # Search for student
        for student in students:

            if student["roll_no"] == delete_roll_no:

                # Remove student from list
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