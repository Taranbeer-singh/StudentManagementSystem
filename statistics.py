# Student statistics functions


def get_overall_statistics(students):

    if len(students) == 0:
        return 0, 0, 0, 0


    total_marks = []

    for student in students:

        for mark in student["marks"].values():

            total_marks.append(mark)


    total_students = len(students)

    average_marks = sum(total_marks) / len(total_marks)

    highest_marks = max(total_marks)

    lowest_marks = min(total_marks)


    return (
        total_students,
        average_marks,
        highest_marks,
        lowest_marks
    )


def get_course_statistics(students):

    course_count = {}

    for student in students:

        course = student["course"]

        if course in course_count:

            course_count[course] += 1

        else:

            course_count[course] = 1

    return course_count


def get_year_statistics(students):

    year_count = {}

    for student in students:

        year = student["year"]

        if year in year_count:

            year_count[year] += 1

        else:

            year_count[year] = 1

    return year_count


def get_student_marks_statistics(student):

    marks = student["marks"]

    total_marks = len(marks) * 100

    obtained_marks = sum(marks.values())

    percentage = (obtained_marks / total_marks) * 100

    return total_marks, obtained_marks, percentage


def get_subject_statistics(students):

    subject_marks = {}

    for student in students:

        for subject, marks in student["marks"].items():

            if subject in subject_marks:

                subject_marks[subject].append(marks)

            else:

                subject_marks[subject] = [marks]


    subject_average = {}

    for subject, marks_list in subject_marks.items():

        average = sum(marks_list) / len(marks_list)

        subject_average[subject] = average


    return subject_average


# ==============================
# Top Performing Students
# ==============================

def get_top_students(students, limit=5):

    student_results = []


    for student in students:

        marks = student["marks"]


        if not marks:
            continue


        total_marks = len(marks) * 100

        obtained_marks = sum(marks.values())

        percentage = (
            obtained_marks / total_marks
        ) * 100


        student_results.append({

            "name": student["name"],

            "roll_no": student["roll_no"],

            "percentage": percentage
        })


    # Sort students by percentage
    student_results.sort(
        key=lambda student: student["percentage"],
        reverse=True
    )


    return student_results[:limit]


# ==============================
# Pass / Fail Statistics
# ==============================

def get_pass_fail_statistics(
    students,
    pass_percentage=40
):

    passed = 0

    failed = 0


    for student in students:

        marks = student["marks"]


        if not marks:
            continue


        total_marks = len(marks) * 100

        obtained_marks = sum(marks.values())


        percentage = (
            obtained_marks / total_marks
        ) * 100


        if percentage >= pass_percentage:

            passed += 1

        else:

            failed += 1


    total_evaluated = passed + failed


    if total_evaluated == 0:

        return {
            "passed": 0,
            "failed": 0,
            "pass_percentage": 0,
            "fail_percentage": 0
        }


    pass_percentage_value = (
        passed / total_evaluated
    ) * 100


    fail_percentage_value = (
        failed / total_evaluated
    ) * 100


    return {

        "passed": passed,

        "failed": failed,

        "pass_percentage": pass_percentage_value,

        "fail_percentage": fail_percentage_value
    }