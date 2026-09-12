import tkinter as tk

from database import get_all_students

from statistics import (
    get_overall_statistics,
    get_course_statistics,
    get_year_statistics,
    get_subject_statistics,
    get_top_students,
    get_pass_fail_statistics
)


class StatisticsPage:

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
    # Show Statistics Page
    # ==============================

    def show(self):

        self.clear_page()


        students = get_all_students()


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Statistics",
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
            text="View academic and student distribution statistics",
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
        # Empty Database
        # ==============================

        if not students:

            self.show_empty_message()

            return


        # ==============================
        # Overall Statistics
        # ==============================

        (
            total_students,
            average_marks,
            highest_marks,
            lowest_marks
        ) = get_overall_statistics(
            students
        )


        # ==============================
        # Statistics Cards
        # ==============================

        statistics_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        statistics_frame.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        self.create_stat_card(
            statistics_frame,
            "Total Students",
            total_students
        )


        self.create_stat_card(
            statistics_frame,
            "Average Marks",
            f"{average_marks:.2f}"
        )


        self.create_stat_card(
            statistics_frame,
            "Highest Marks",
            highest_marks
        )


        self.create_stat_card(
            statistics_frame,
            "Lowest Marks",
            lowest_marks
        )


        # ==============================
        # Course Statistics
        # ==============================

        course_statistics = get_course_statistics(
            students
        )


        self.create_distribution_card(
            "Students by Course",
            course_statistics
        )


        # ==============================
        # Year Statistics
        # ==============================

        year_statistics = get_year_statistics(
            students
        )


        self.create_distribution_card(
            "Students by Year",
            year_statistics
        )


        # ==============================
        # Subject Statistics
        # ==============================

        subject_statistics = get_subject_statistics(
            students
        )


        self.create_subject_statistics_card(
            subject_statistics
        )


        # ==============================
        # Top Performing Students
        # ==============================

        top_students = get_top_students(
            students
        )


        self.create_top_students_card(
            top_students
        )


        # ==============================
        # Pass / Fail Statistics
        # ==============================

        pass_fail_statistics = get_pass_fail_statistics(
            students
        )


        self.create_pass_fail_card(
            pass_fail_statistics
        )


    # ==============================
    # Statistic Card
    # ==============================

    def create_stat_card(
        self,
        parent,
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
            padx=5
        )


        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        title_label.pack(
            pady=(18, 5)
        )


        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 22, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        value_label.pack(
            pady=(0, 18)
        )


    # ==============================
    # Distribution Card
    # ==============================

    def create_distribution_card(
        self,
        title,
        statistics
    ):

        card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            fill="x",
            padx=40,
            pady=(0, 20)
        )


        # ==============================
        # Card Heading
        # ==============================

        heading = tk.Label(
            card,
            text=title,
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Statistics Rows
        # ==============================

        for name, count in statistics.items():

            row = tk.Frame(
                card,
                bg=self.card_color
            )

            row.pack(
                fill="x",
                padx=25,
                pady=6
            )


            name_label = tk.Label(
                row,
                text=name,
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.text_color,
                anchor="w"
            )

            name_label.pack(
                side="left"
            )


            count_label = tk.Label(
                row,
                text=str(count),
                font=("Arial", 11, "bold"),
                bg=self.card_color,
                fg=self.text_color,
                anchor="e"
            )

            count_label.pack(
                side="right"
            )


        spacer = tk.Frame(
            card,
            bg=self.card_color,
            height=10
        )

        spacer.pack()


    # ==============================
    # Subject Statistics Card
    # ==============================

    def create_subject_statistics_card(
        self,
        statistics
    ):

        card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            fill="x",
            padx=40,
            pady=(0, 20)
        )


        # ==============================
        # Card Heading
        # ==============================

        heading = tk.Label(
            card,
            text="Subject-wise Average Marks",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Subject Rows
        # ==============================

        for subject, average in statistics.items():

            row = tk.Frame(
                card,
                bg=self.card_color
            )

            row.pack(
                fill="x",
                padx=25,
                pady=6
            )


            subject_label = tk.Label(
                row,
                text=subject,
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.text_color,
                anchor="w"
            )

            subject_label.pack(
                side="left"
            )


            average_label = tk.Label(
                row,
                text=f"{average:.2f}%",
                font=("Arial", 11, "bold"),
                bg=self.card_color,
                fg=self.text_color,
                anchor="e"
            )

            average_label.pack(
                side="right"
            )


        spacer = tk.Frame(
            card,
            bg=self.card_color,
            height=10
        )

        spacer.pack()


    # ==============================
    # Top Students Card
    # ==============================

    def create_top_students_card(
        self,
        students
    ):

        card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            fill="x",
            padx=40,
            pady=(0, 20)
        )


        # ==============================
        # Card Heading
        # ==============================

        heading = tk.Label(
            card,
            text="Top Performing Students",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Student Rows
        # ==============================

        for index, student in enumerate(
            students,
            start=1
        ):

            row = tk.Frame(
                card,
                bg=self.card_color
            )

            row.pack(
                fill="x",
                padx=25,
                pady=6
            )


            rank_label = tk.Label(
                row,
                text=f"#{index}",
                font=("Arial", 11, "bold"),
                bg=self.card_color,
                fg=self.text_color,
                width=5,
                anchor="w"
            )

            rank_label.pack(
                side="left"
            )


            name_label = tk.Label(
                row,
                text=student["name"],
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.text_color,
                anchor="w"
            )

            name_label.pack(
                side="left"
            )


            roll_label = tk.Label(
                row,
                text=f"Roll No: {student['roll_no']}",
                font=("Arial", 10),
                bg=self.card_color,
                fg=self.secondary_text
            )

            roll_label.pack(
                side="right",
                padx=(0, 20)
            )


            percentage_label = tk.Label(
                row,
                text=f"{student['percentage']:.2f}%",
                font=("Arial", 11, "bold"),
                bg=self.card_color,
                fg=self.text_color
            )

            percentage_label.pack(
                side="right"
            )


        spacer = tk.Frame(
            card,
            bg=self.card_color,
            height=10
        )

        spacer.pack()


    # ==============================
    # Pass / Fail Card
    # ==============================

    def create_pass_fail_card(
        self,
        statistics
    ):

        card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            fill="x",
            padx=40,
            pady=(0, 40)
        )


        # ==============================
        # Card Heading
        # ==============================

        heading = tk.Label(
            card,
            text="Pass / Fail Statistics",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Pass / Fail Cards
        # ==============================

        statistics_frame = tk.Frame(
            card,
            bg=self.card_color
        )

        statistics_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )


        self.create_inner_stat_card(
            statistics_frame,
            "Passed",
            statistics["passed"],
            f"{statistics['pass_percentage']:.2f}%"
        )


        self.create_inner_stat_card(
            statistics_frame,
            "Failed",
            statistics["failed"],
            f"{statistics['fail_percentage']:.2f}%"
        )


    # ==============================
    # Inner Statistic Card
    # ==============================

    def create_inner_stat_card(
        self,
        parent,
        title,
        count,
        percentage
    ):

        card = tk.Frame(
            parent,
            bg=self.background_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )


        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        title_label.pack(
            pady=(15, 3)
        )


        count_label = tk.Label(
            card,
            text=str(count),
            font=("Arial", 22, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        count_label.pack()


        percentage_label = tk.Label(
            card,
            text=percentage,
            font=("Arial", 10),
            bg=self.background_color,
            fg=self.secondary_text
        )

        percentage_label.pack(
            pady=(0, 15)
        )


    # ==============================
    # Empty Message
    # ==============================

    def show_empty_message(self):

        empty_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        empty_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        icon = tk.Label(
            empty_card,
            text="📊",
            font=("Arial", 28),
            bg=self.card_color
        )

        icon.pack(
            pady=(25, 5)
        )


        title = tk.Label(
            empty_card,
            text="No Statistics Available",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        title.pack()


        message = tk.Label(
            empty_card,
            text="Add students to view statistics.",
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        message.pack(
            pady=(5, 25)
        )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()