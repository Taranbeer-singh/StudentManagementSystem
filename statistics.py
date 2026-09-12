# Student Statistics Functions

from courses import courses


def get_overall_statistics(students):

    total_students = len(students)

    total_marks = 0
    total_subjects = 0

    highest_marks = 0
    lowest_marks = 0

    student_total_marks = []

    for student in students:

        marks = student["marks"]

        if marks:

            student_total = sum(marks.values())

            total_marks += student_total
            total_subjects += len(marks)

            student_total_marks.append(
                student_total
            )

    if total_subjects == 0:

        average_marks = 0

    else:

        average_marks = (
            total_marks /
            total_subjects
        )

    if student_total_marks:

        highest_marks = max(
            student_total_marks
        )

        lowest_marks = min(
            student_total_marks
        )

    return (
        total_students,
        average_marks,
        highest_marks,
        lowest_marks
    )


def get_course_statistics(students):

    # Always show every course defined
    # in courses.py.

    course_count = {
        course: 0
        for course in courses
    }

    for student in students:

        course = student["course"]

        if course in course_count:

            course_count[course] += 1

        else:

            # Handles any unexpected course
            # already present in the database.

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

    if not marks:

        return 0, 0, 0

    total_marks = sum(
        marks.values()
    )

    total_subjects = len(marks)

    maximum_marks = (
        total_subjects * 100
    )

    percentage = (
        total_marks /
        maximum_marks
    ) * 100

    return (
        total_marks,
        maximum_marks,
        percentage
    )


def get_student_status(
    student,
    pass_percentage=40
):

    _, _, percentage = (
        get_student_marks_statistics(
            student
        )
    )

    if not student["marks"]:

        return "N/A"

    if percentage >= pass_percentage:

        return "Pass"

    return "Fail"


def get_subject_statistics(students):

    subject_marks = {}

    for student in students:

        for subject, marks in (
            student["marks"].items()
        ):

            if subject in subject_marks:

                subject_marks[subject].append(
                    marks
                )

            else:

                subject_marks[subject] = [
                    marks
                ]

    subject_average = {}

    for subject, marks_list in (
        subject_marks.items()
    ):

        average = (
            sum(marks_list) /
            len(marks_list)
        )

        subject_average[subject] = average

    return subject_average


def get_course_subject_statistics(students):

    course_subject_marks = {}

    for student in students:

        course = student["course"]

        if course not in course_subject_marks:

            course_subject_marks[course] = {}

        for subject, marks in (
            student["marks"].items()
        ):

            if (
                subject
                in course_subject_marks[course]
            ):

                course_subject_marks[
                    course
                ][subject].append(
                    marks
                )

            else:

                course_subject_marks[
                    course
                ][subject] = [
                    marks
                ]

    course_subject_average = {}

    for course, subjects in (
        course_subject_marks.items()
    ):

        course_subject_average[course] = {}

        for subject, marks_list in (
            subjects.items()
        ):

            average = (
                sum(marks_list) /
                len(marks_list)
            )

            course_subject_average[
                course
            ][subject] = average

    return course_subject_average


def get_top_students(
    students,
    limit=5
):

    student_percentages = []

    for student in students:

        _, _, percentage = (
            get_student_marks_statistics(
                student
            )
        )

        student_percentages.append(
            {
                "name": student["name"],
                "roll_no": student["roll_no"],
                "course": student["course"],
                "percentage": percentage
            }
        )

    student_percentages.sort(
        key=lambda student: student["percentage"],
        reverse=True
    )

    return student_percentages[:limit]


def get_pass_fail_statistics(students):

    passed = 0
    failed = 0
    not_available = 0

    for student in students:

        status = get_student_status(
            student
        )

        if status == "Pass":

            passed += 1

        elif status == "Fail":

            failed += 1

        else:

            not_available += 1

    total_students = (
        passed +
        failed
    )

    if total_students == 0:

        pass_percentage = 0
        fail_percentage = 0

    else:

        pass_percentage = (
            passed /
            total_students
        ) * 100

        fail_percentage = (
            failed /
            total_students
        ) * 100

    return {
        "passed": passed,
        "failed": failed,
        "N/A": not_available,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage
    }