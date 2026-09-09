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

