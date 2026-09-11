import tkinter as tk

from courses import courses
from database import get_all_students
from statistics import get_overall_statistics, get_student_marks_statistics


class DashboardPage:

    def __init__(
        self,
        parent,
        background_color,
        card_color,
        text_color,
        secondary_text
    ):

        self.parent = parent

        self.background_color = background_color
        self.card_color = card_color
        self.text_color = text_color
        self.secondary_text = secondary_text


    # ==============================
    # Show Dashboard
    # ==============================

    def show(self):

        self.clear_page()

        students = get_all_students()


        # ==============================
        # Dashboard Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Dashboard",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.parent,
            text="Overview of your student management system",
            font=("Arial", 12),
            bg=self.background_color,
            fg=self.secondary_text
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
        )


        # ==============================
        # Calculate Statistics
        # ==============================

        total_students = len(students)


        total_courses = len(courses)


        if students:

            statistics = get_overall_statistics(
                students
            )

            average_marks = statistics[1]

        else:

            average_marks = 0


        # ==============================
        # Statistics Cards
        # ==============================

        cards_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        cards_frame.pack(
            fill="x",
            padx=34
        )


        self.create_stat_card(
            cards_frame,
            "👨‍🎓",
            "Total Students",
            total_students
        )

        self.create_stat_card(
            cards_frame,
            "📚",
            "Total Courses",
            total_courses
        )

        self.create_stat_card(
            cards_frame,
            "📊",
            "Average Marks",
            f"{average_marks:.2f}%"
        )


        # ==============================
        # Available Courses
        # ==============================

        courses_title = tk.Label(
            self.parent,
            text="Available Courses",
            font=("Arial", 19, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        courses_title.pack(
            anchor="w",
            padx=40,
            pady=(35, 15)
        )


        courses_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        courses_frame.pack(
            fill="x",
            padx=34
        )


        # ==============================
        # Course Student Counts
        # ==============================

        course_student_counts = {}

        for course_name in courses:

            course_student_counts[course_name] = 0


        for student in students:

            student_course = student["course"]

            if student_course in course_student_counts:

                course_student_counts[student_course] += 1


        # ==============================
        # Display Courses
        # ==============================

        for course_name in courses:

            student_count = course_student_counts[
                course_name
            ]


            course_card = tk.Frame(
                courses_frame,
                bg=self.card_color,
                highlightthickness=1,
                highlightbackground="#e2e8f0"
            )

            course_card.pack(
                fill="x",
                padx=6,
                pady=5
            )


            # Course icon

            course_icon = tk.Label(
                course_card,
                text="🎓",
                font=("Arial", 20),
                bg=self.card_color
            )

            course_icon.pack(
                side="left",
                padx=(18, 10),
                pady=12
            )


            # Course name

            course_name_label = tk.Label(
                course_card,
                text=course_name,
                font=("Arial", 12, "bold"),
                bg=self.card_color,
                fg=self.text_color
            )

            course_name_label.pack(
                side="left",
                pady=12
            )


            # Student count

            student_text = (
                f"{student_count} student"
                if student_count == 1
                else f"{student_count} students"
            )


            count_label = tk.Label(
                course_card,
                text=student_text,
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.secondary_text
            )

            count_label.pack(
                side="right",
                padx=20
            )


        # ==============================
        # Recent Students
        # ==============================

        recent_title = tk.Label(
            self.parent,
            text="Recent Students",
            font=("Arial", 19, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        recent_title.pack(
            anchor="w",
            padx=40,
            pady=(35, 15)
        )


        table_frame = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        table_frame.pack(
            fill="x",
            padx=40
        )


        # ==============================
        # Table Headers
        # ==============================

        headers = [
            "Name",
            "Roll No.",
            "Course",
            "Year",
            "Percentage"
        ]


        for column, header in enumerate(headers):

            label = tk.Label(
                table_frame,
                text=header,
                font=("Arial", 11, "bold"),
                bg=self.card_color,
                fg=self.secondary_text,
                anchor="w"
            )

            label.grid(
                row=0,
                column=column,
                padx=15,
                pady=12,
                sticky="w"
            )


        # ==============================
        # Recent Student Data
        # ==============================

        if students:

            recent_students = students[-5:]


            for row, student in enumerate(
                recent_students,
                start=1
            ):

                _, _, percentage = get_student_marks_statistics(
                    student
                )


                values = [
                    student["name"],
                    student["roll_no"],
                    student["course"],
                    student["year"],
                    f"{percentage:.2f}%"
                ]


                for column, value in enumerate(values):

                    label = tk.Label(
                        table_frame,
                        text=value,
                        font=("Arial", 11),
                        bg=self.card_color,
                        fg=self.text_color,
                        anchor="w"
                    )

                    label.grid(
                        row=row,
                        column=column,
                        padx=15,
                        pady=10,
                        sticky="w"
                    )

        else:

            empty_label = tk.Label(
                table_frame,
                text="No students found.",
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.secondary_text
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=5,
                pady=20
            )


    # ==============================
    # Statistics Card
    # ==============================

    def create_stat_card(
        self,
        parent,
        icon,
        title,
        value
    ):

        card = tk.Frame(
            parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=6
        )


        icon_label = tk.Label(
            card,
            text=icon,
            font=("Arial", 22),
            bg=self.card_color
        )

        icon_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 5)
        )


        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        title_label.pack(
            anchor="w",
            padx=20
        )


        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 23, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        value_label.pack(
            anchor="w",
            padx=20,
            pady=(3, 18)
        )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()