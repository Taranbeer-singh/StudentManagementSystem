import tkinter as tk

from database import get_all_students
from statistics import get_overall_statistics, get_student_marks_statistics


class DashboardApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Student Management System"
        )

        self.root.geometry(
            "1100x700"
        )

        self.root.minsize(
            900,
            600
        )

        # ==============================
        # Colors
        # ==============================

        self.sidebar_color = "#1e293b"
        self.sidebar_hover = "#334155"
        self.background_color = "#f1f5f9"
        self.card_color = "#ffffff"
        self.text_color = "#0f172a"
        self.secondary_text = "#64748b"


        # ==============================
        # Main Layout
        # ==============================

        self.sidebar = tk.Frame(
            self.root,
            width=220,
            bg=self.sidebar_color
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(
            False
        )


        self.content = tk.Frame(
            self.root,
            bg=self.background_color
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )


        # ==============================
        # Application Title
        # ==============================

        title = tk.Label(
            self.sidebar,
            text="🎓 Student\nManagement System",
            font=("Arial", 17, "bold"),
            bg=self.sidebar_color,
            fg="white",
            justify="left"
        )

        title.pack(
            anchor="w",
            padx=22,
            pady=(35, 45)
        )


        # ==============================
        # Main Navigation Area
        # ==============================

        navigation_frame = tk.Frame(
            self.sidebar,
            bg=self.sidebar_color
        )

        navigation_frame.pack(
            fill="x"
        )


        self.create_navigation_button(
            navigation_frame,
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.create_navigation_button(
            navigation_frame,
            "👨‍🎓  Students",
            self.show_students
        )

        self.create_navigation_button(
            navigation_frame,
            "➕  Add Student",
            self.show_add_student
        )

        self.create_navigation_button(
            navigation_frame,
            "🔍  Search",
            self.show_search
        )

        self.create_navigation_button(
            navigation_frame,
            "📊  Statistics",
            self.show_statistics
        )


        # ==============================
        # Bottom Spacer
        # ==============================

        spacer = tk.Frame(
            self.sidebar,
            bg=self.sidebar_color
        )

        spacer.pack(
            fill="both",
            expand=True
        )


        # ==============================
        # Settings at Bottom
        # ==============================

        settings_frame = tk.Frame(
            self.sidebar,
            bg=self.sidebar_color
        )

        settings_frame.pack(
            fill="x",
            padx=0,
            pady=(0, 20)
        )


        self.create_navigation_button(
            settings_frame,
            "⚙️  Settings",
            self.show_settings
        )


        # ==============================
        # Show Dashboard
        # ==============================

        self.show_dashboard()


    # ==============================
    # Navigation Button
    # ==============================

    def create_navigation_button(
        self,
        parent,
        text,
        command
    ):

        button_frame = tk.Frame(
            parent,
            bg=self.sidebar_color,
            cursor="hand2"
        )

        button_frame.pack(
            fill="x",
            padx=12,
            pady=5
        )


        button_label = tk.Label(
            button_frame,
            text=text,
            font=("Arial", 13),
            bg=self.sidebar_color,
            fg="white",
            anchor="w",
            padx=15,
            pady=14,
            cursor="hand2"
        )

        button_label.pack(
            fill="x"
        )


        # ==============================
        # Click Event
        # ==============================

        button_frame.bind(
            "<Button-1>",
            lambda event: command()
        )

        button_label.bind(
            "<Button-1>",
            lambda event: command()
        )


        # ==============================
        # Hover Effect
        # ==============================

        button_frame.bind(
            "<Enter>",
            lambda event: self.navigation_hover(
                button_frame,
                button_label,
                True
            )
        )

        button_frame.bind(
            "<Leave>",
            lambda event: self.navigation_hover(
                button_frame,
                button_label,
                False
            )
        )

        button_label.bind(
            "<Enter>",
            lambda event: self.navigation_hover(
                button_frame,
                button_label,
                True
            )
        )

        button_label.bind(
            "<Leave>",
            lambda event: self.navigation_hover(
                button_frame,
                button_label,
                False
            )
        )


    # ==============================
    # Navigation Hover
    # ==============================

    def navigation_hover(
        self,
        frame,
        label,
        hovering
    ):

        if hovering:

            frame.config(
                bg=self.sidebar_hover
            )

            label.config(
                bg=self.sidebar_hover
            )

        else:

            frame.config(
                bg=self.sidebar_color
            )

            label.config(
                bg=self.sidebar_color
            )


    # ==============================
    # Clear Content
    # ==============================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()


    # ==============================
    # Dashboard
    # ==============================

    def show_dashboard(self):

        self.clear_content()

        students = get_all_students()


        # ==============================
        # Dashboard Header
        # ==============================

        heading = tk.Label(
            self.content,
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
            self.content,
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


        courses = set()

        for student in students:

            courses.add(
                student["course"]
            )


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
            self.content,
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
        # Recent Students
        # ==============================

        recent_title = tk.Label(
            self.content,
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
            self.content,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        table_frame.pack(
            fill="x",
            padx=40
        )


        # ==============================
        # Table Header
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
        # Student Rows
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
    # Students Page
    # ==============================

    def show_students(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Students",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Student list will appear here.",
            font=("Arial", 16),
            bg=self.background_color,
            fg=self.secondary_text
        )

        message.pack(
            anchor="w",
            padx=40
        )


    # ==============================
    # Add Student Page
    # ==============================

    def show_add_student(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Add Student",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Add Student form will appear here.",
            font=("Arial", 16),
            bg=self.background_color,
            fg=self.secondary_text
        )

        message.pack(
            anchor="w",
            padx=40
        )


    # ==============================
    # Search Page
    # ==============================

    def show_search(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Search Student",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Search functionality will appear here.",
            font=("Arial", 16),
            bg=self.background_color,
            fg=self.secondary_text
        )

        message.pack(
            anchor="w",
            padx=40
        )


    # ==============================
    # Statistics Page
    # ==============================

    def show_statistics(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Statistics",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Statistics dashboard will appear here.",
            font=("Arial", 16),
            bg=self.background_color,
            fg=self.secondary_text
        )

        message.pack(
            anchor="w",
            padx=40
        )


    # ==============================
    # Settings Page
    # ==============================

    def show_settings(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Settings",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Settings will appear here.",
            font=("Arial", 16),
            bg=self.background_color,
            fg=self.secondary_text
        )

        message.pack(
            anchor="w",
            padx=40
        )


# ==============================
# Start Application
# ==============================

if __name__ == "__main__":

    root = tk.Tk()

    app = DashboardApp(root)

    root.mainloop()