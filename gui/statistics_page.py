import tkinter as tk

from database import get_all_students

from statistics import (
    get_overall_statistics,
    get_course_statistics,
    get_year_statistics,
    get_course_subject_statistics,
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
        # Statistics Data
        # ==============================

        course_statistics = get_course_statistics(
            students
        )

        year_statistics = get_year_statistics(
            students
        )

        course_subject_statistics = (
            get_course_subject_statistics(
                students
            )
        )

        pass_fail_statistics = (
            get_pass_fail_statistics(
                students
            )
        )


        # ==============================
        # Course + Year Charts
        # ==============================

        charts_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        charts_frame.pack(
            fill="x",
            padx=40,
            pady=(0, 20)
        )


        self.create_chart_card(
            charts_frame,
            "Students by Course",
            course_statistics
        )


        self.create_chart_card(
            charts_frame,
            "Students by Year",
            year_statistics
        )


        # ==============================
        # Course-wise Subject Charts
        # ==============================

        subject_heading = tk.Label(
            self.parent,
            text="Subject-wise Average Marks",
            font=("Arial", 20, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        subject_heading.pack(
            anchor="w",
            padx=40,
            pady=(10, 15)
        )


        for course, subjects in (
            course_subject_statistics.items()
        ):

            self.create_course_subject_card(
                course,
                subjects
            )


        # ==============================
        # Pass / Fail Chart
        # ==============================

        pass_fail_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        pass_fail_frame.pack(
            fill="x",
            padx=40,
            pady=(5, 20)
        )


        self.create_pass_fail_chart_card(
            pass_fail_frame,
            pass_fail_statistics
        )


        # ==============================
        # Top Students
        # ==============================

        top_students = get_top_students(
            students
        )


        self.create_top_students_card(
            top_students
        )


        # ==============================
        # Pass / Fail Summary
        # ==============================

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
    # Generic Chart Card
    # ==============================

    def create_chart_card(
        self,
        parent,
        title,
        statistics
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


        heading = tk.Label(
            card,
            text=title,
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )


        canvas = tk.Canvas(
            card,
            height=260,
            bg=self.card_color,
            highlightthickness=0
        )

        canvas.pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )


        self.draw_bar_chart(
            canvas,
            statistics
        )


    # ==============================
    # Course Subject Card
    # ==============================

    def create_course_subject_card(
        self,
        course,
        subjects
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


        heading = tk.Label(
            card,
            text=course,
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )


        canvas = tk.Canvas(
            card,
            height=260,
            bg=self.card_color,
            highlightthickness=0
        )

        canvas.pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )


        self.draw_bar_chart(
            canvas,
            subjects,
            percentage=True
        )


    # ==============================
    # Pass / Fail Chart
    # ==============================

    def create_pass_fail_chart_card(
        self,
        parent,
        statistics
    ):

        card = tk.Frame(
            parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        card.pack(
            fill="both",
            expand=True,
            padx=5
        )


        heading = tk.Label(
            card,
            text="Pass / Fail Distribution",
            font=("Arial", 16, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )


        canvas = tk.Canvas(
            card,
            height=260,
            bg=self.card_color,
            highlightthickness=0
        )

        canvas.pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )


        chart_data = {
            "Passed": statistics["passed"],
            "Failed": statistics["failed"]
        }


        self.draw_bar_chart(
            canvas,
            chart_data
        )


    # ==============================
    # Draw Bar Chart
    # ==============================

    def draw_bar_chart(
        self,
        canvas,
        statistics,
        percentage=False
    ):

        canvas.update_idletasks()


        width = max(
            canvas.winfo_width(),
            400
        )

        height = 260


        left_margin = 45
        right_margin = 20
        top_margin = 20
        bottom_margin = 55


        chart_width = (
            width
            - left_margin
            - right_margin
        )

        chart_height = (
            height
            - top_margin
            - bottom_margin
        )


        if not statistics:

            canvas.create_text(
                width / 2,
                height / 2,
                text="No data available",
                fill=self.secondary_text,
                font=("Arial", 10)
            )

            return


        maximum = max(
            statistics.values()
        )


        if maximum <= 0:

            maximum = 1


        # ==============================
        # Axis
        # ==============================

        canvas.create_line(
            left_margin,
            top_margin,
            left_margin,
            height - bottom_margin,
            fill="#cbd5e1"
        )


        canvas.create_line(
            left_margin,
            height - bottom_margin,
            width - right_margin,
            height - bottom_margin,
            fill="#cbd5e1"
        )


        count = len(statistics)

        spacing = chart_width / count

        bar_width = min(
            55,
            spacing * 0.55
        )


        for index, (name, value) in enumerate(
            statistics.items()
        ):

            bar_height = (
                value / maximum
            ) * chart_height


            x_center = (
                left_margin
                + spacing * index
                + spacing / 2
            )


            x1 = (
                x_center -
                bar_width / 2
            )

            x2 = (
                x_center +
                bar_width / 2
            )


            y1 = (
                height
                - bottom_margin
                - bar_height
            )

            y2 = (
                height
                - bottom_margin
            )


            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="#3b82f6",
                outline=""
            )


            # ==============================
            # Value
            # ==============================

            if percentage:

                value_text = f"{value:.1f}%"

            elif isinstance(value, float):

                value_text = f"{value:.1f}"

            else:

                value_text = str(value)


            canvas.create_text(
                x_center,
                y1 - 10,
                text=value_text,
                fill=self.text_color,
                font=("Arial", 9, "bold")
            )


            # ==============================
            # Label
            # ==============================

            label_text = str(name)


            if len(label_text) > 16:

                label_text = (
                    label_text[:15]
                    + "..."
                )


            canvas.create_text(
                x_center,
                height - bottom_margin + 18,
                text=label_text,
                fill=self.secondary_text,
                font=("Arial", 9)
            )


        # ==============================
        # Maximum Value
        # ==============================

        if percentage:

            maximum_text = f"{maximum:.0f}%"

        else:

            maximum_text = str(
                int(maximum)
                if maximum == int(maximum)
                else round(maximum, 1)
            )


        canvas.create_text(
            left_margin - 8,
            top_margin,
            text=maximum_text,
            fill=self.secondary_text,
            font=("Arial", 8),
            anchor="e"
        )


        canvas.create_text(
            left_margin - 8,
            height - bottom_margin,
            text="0",
            fill=self.secondary_text,
            font=("Arial", 8),
            anchor="e"
        )


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
    # Pass / Fail Summary
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