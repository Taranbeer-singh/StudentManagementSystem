print("========================================")
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
    print("Add Student selected")

    name = input("Enter Student Name:")
    roll_No = int(input("Enter Student Roll No.:"))
    course = input("Enter Student Course:")
    age = int(input("Enter Student Age:"))
    marks = int(input("Enter Student Marks:"))
    print("\nStudent added successfully!")

elif choice == "2":
    print("View Students selected")

elif choice == "3":
    print("Search Student selected")

elif choice == "4":
    print("Update Student selected")

elif choice == "5":
    print("Delete Student selected")

elif choice == "6":
    print("Exiting Student Management System...")

else:
    print("Invalid choice!")