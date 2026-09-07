# Validation functions


def get_valid_name(prompt):

    while True:

        name = input(prompt)

        if name.strip() == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name can contain only letters and spaces.")
            continue

        return name


def get_valid_roll_no(prompt, students=None):

    while True:

        try:
            roll_no = int(input(prompt))

            if roll_no <= 0:
                print("Roll No. must be greater than 0.")
                continue

            # Check duplicate roll number only when students are provided
            if students is not None:

                duplicate = False

                for student in students:

                    if student["roll_no"] == roll_no:
                        duplicate = True
                        break

                if duplicate:
                    print("Roll No. already exists.")
                    continue

            return roll_no

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_valid_course(prompt):

    while True:

        course = input(prompt)

        if course.strip() == "":
            print("Course cannot be empty.")
            continue

        if not course.replace(" ", "").isalpha():
            print("Course can contain only letters and spaces.")
            continue

        return course


def get_valid_age(prompt):

    while True:

        try:
            age = int(input(prompt))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            return age

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_valid_marks(prompt):

    while True:

        try:
            marks = int(input(prompt))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue

            return marks

        except ValueError:
            print("Invalid input! Please enter a number.")