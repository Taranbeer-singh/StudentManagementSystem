import tkinter as tk

from courses import courses


class AddStudentPage:

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

        self.subject_entries = {}


    # ==============================
    # Show Add Student Page
    # ==============================

    def show(self):

        self.clear_page()

        self.subject_entries = {}


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Add Student",
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
            text="Add a new student to the system",
            font=("Arial", 12),
            bg=self.background_color,
            fg=self.secondary_text
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 30)
        )


        # ==============================
        # Personal Information
        # ==============================

        section_title = tk.Label(
            self.parent,
            text="Personal Information",
            font=("Arial", 18, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        section_title.pack(
            anchor="w",
            padx=40,
            pady=(0, 12)
        )


        # ==============================
        # Personal Information Card
        # ==============================

        form_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        form_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        # ==============================
        # Name
        # ==============================

        self.create_label(
            form_card,
            "Student Name"
        )


        self.name_entry = tk.Entry(
            form_card,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.name_entry.pack(
            fill="x",
            padx=20,
            pady=(0, 15),
            ipady=7
        )


        # ==============================
        # Roll Number
        # ==============================

        self.create_label(
            form_card,
            "Roll Number"
        )


        self.roll_entry = tk.Entry(
            form_card,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.roll_entry.pack(
            fill="x",
            padx=20,
            pady=(0, 15),
            ipady=7
        )


        # ==============================
        # Age
        # ==============================

        self.create_label(
            form_card,
            "Age"
        )


        self.age_entry = tk.Entry(
            form_card,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.age_entry.pack(
            fill="x",
            padx=20,
            pady=(0, 15),
            ipady=7
        )


        # ==============================
        # Course
        # ==============================

        self.create_label(
            form_card,
            "Course"
        )


        self.course_var = tk.StringVar(
            value="Select Course"
        )


        self.course_menu = tk.OptionMenu(
            form_card,
            self.course_var,
            "Select Course",
            *courses.keys(),
            command=self.course_selected
        )

        self.course_menu.config(
            font=("Arial", 11),
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black",
            relief="solid",
            bd=1,
            anchor="w"
        )

        self.course_menu["menu"].config(
            font=("Arial", 11),
            bg="white",
            fg="black"
        )

        self.course_menu.pack(
            fill="x",
            padx=20,
            pady=(0, 15),
            ipady=4
        )


        # ==============================
        # Year
        # ==============================

        self.create_label(
            form_card,
            "Year"
        )


        self.year_var = tk.StringVar(
            value="Select Year"
        )


        self.year_menu = tk.OptionMenu(
            form_card,
            self.year_var,
            "Select Year",
            command=self.year_selected
        )

        self.year_menu.config(
            font=("Arial", 11),
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black",
            relief="solid",
            bd=1,
            anchor="w"
        )

        self.year_menu["menu"].config(
            font=("Arial", 11),
            bg="white",
            fg="black"
        )

        self.year_menu.pack(
            fill="x",
            padx=20,
            pady=(0, 20),
            ipady=4
        )


        # ==============================
        # Subjects & Marks
        # ==============================

        marks_title = tk.Label(
            self.parent,
            text="Subjects & Marks",
            font=("Arial", 18, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        marks_title.pack(
            anchor="w",
            padx=40,
            pady=(0, 12)
        )


        self.marks_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        self.marks_card.pack(
            fill="x",
            padx=40,
            pady=(0, 30)
        )


        self.placeholder_label = tk.Label(
            self.marks_card,
            text="Select a course and year to add subject marks.",
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        self.placeholder_label.pack(
            anchor="w",
            padx=20,
            pady=20
        )


    # ==============================
    # Course Selected
    # ==============================

    def course_selected(self, selected_course):

        # Reset year selection

        self.year_var.set(
            "Select Year"
        )


        # Clear old year options

        menu = self.year_menu["menu"]

        menu.delete(
            0,
            "end"
        )


        # Add available years

        menu.add_command(
            label="Select Year",
            command=lambda: self.year_var.set(
                "Select Year"
            )
        )


        for year in courses[selected_course]:

            menu.add_command(
                label=year,
                command=lambda value=year:
                    self.year_selected(value)
            )


        # Clear subjects until year is selected

        self.clear_subjects()


    # ==============================
    # Year Selected
    # ==============================

    def year_selected(self, selected_year):

        course = self.course_var.get()


        if course == "Select Course":

            return


        subjects = courses[course][selected_year]


        self.show_subjects(
            subjects
        )


    # ==============================
    # Show Subjects
    # ==============================

    def show_subjects(self, subjects):

        self.clear_subjects()


        # ==============================
        # Header
        # ==============================

        header_frame = tk.Frame(
            self.marks_card,
            bg=self.card_color
        )

        header_frame.pack(
            fill="x",
            padx=20,
            pady=(15, 5)
        )


        subject_header = tk.Label(
            header_frame,
            text="Subject",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.secondary_text,
            anchor="w"
        )

        subject_header.pack(
            side="left"
        )


        marks_header = tk.Label(
            header_frame,
            text="Marks / 100",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.secondary_text
        )

        marks_header.pack(
            side="right",
            padx=5
        )


        # ==============================
        # Subject Rows
        # ==============================

        for subject in subjects:

            row = tk.Frame(
                self.marks_card,
                bg=self.card_color
            )

            row.pack(
                fill="x",
                padx=20,
                pady=7
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


            marks_entry = tk.Entry(
                row,
                font=("Arial", 11),
                bg="white",
                fg="black",
                insertbackground="black",
                relief="solid",
                bd=1,
                width=12
            )

            marks_entry.pack(
                side="right",
                ipady=5
            )


            self.subject_entries[subject] = marks_entry


        # ==============================
        # Bottom Spacing
        # ==============================

        bottom_space = tk.Frame(
            self.marks_card,
            bg=self.card_color,
            height=10
        )

        bottom_space.pack()


    # ==============================
    # Clear Subjects
    # ==============================

    def clear_subjects(self):

        for widget in self.marks_card.winfo_children():

            widget.destroy()


        self.subject_entries = {}


        placeholder = tk.Label(
            self.marks_card,
            text="Select a course and year to add subject marks.",
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        placeholder.pack(
            anchor="w",
            padx=20,
            pady=20
        )


    # ==============================
    # Create Form Label
    # ==============================

    def create_label(
        self,
        parent,
        text
    ):

        label = tk.Label(
            parent,
            text=text,
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color,
            anchor="w"
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(15, 6)
        )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()