
# Store all students in a list
students = []


while True:

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

    elif choice == "3":
        print("\nSearch Student selected")

    elif choice == "4":
        print("\nUpdate Student selected")

    elif choice == "5":
        print("\nDelete Student selected")

    elif choice == "6":
        print("\nExiting Student Management System...")
        break

    else:
        print("\nInvalid choice!") 



 

 
 
