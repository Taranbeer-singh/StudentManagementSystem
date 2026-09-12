import tkinter as tk
from tkinter import messagebox

from courses import courses
from database import get_student_by_roll, update_student


class EditStudentPage:

    def __init__(
        self,
        parent,
        background_color,
        card_color,
        text_color,
        secondary_text,
        back_callback
    ):

        self.parent = parent

        self.background_color = background_color
        self.card_color = card_color
        self.text_color = text_color
        self.secondary_text = secondary_text

        self.back_callback = back_callback

        self.subject_entries = {}

        self.current_student = None
        self.original_roll_no = None


    # ==============================
    # Show Edit Student Page
    # ==============================

    def show(self, roll_no):

        self.clear_page()

        self.subject_entries = {}

        self.original_roll_no = roll_no

        self.current_student = get_student_by_roll(
            roll_no
        )


        # ==============================
        # Student Not Found
        # ==============================

        if self.current_student is None:

            messagebox.showerror(
                "Student Not Found",
                f"No student found with Roll No. {roll_no}."
            )

            return


        student = self.current_student


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Edit Student",
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
            text="Update student information and academic records",
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
        # Personal Information Card
        # ==============================

        personal_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        personal_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        # ==============================
        # Section Title
        # ==============================

        personal_title = tk.Label(
            personal_card,
            text="Personal Information",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        personal_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Name
        # ==============================

        name_label = tk.Label(
            personal_card,
            text="Full Name",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        name_label.pack(
            anchor="w",
            padx=25
        )


        self.name_entry = tk.Entry(
            personal_card,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.name_entry.pack(
            fill="x",
            padx=25,
            pady=(5, 15),
            ipady=7
        )

        self.name_entry.insert(
            0,
            student["name"]
        )


        # ==============================
        # Roll Number
        # ==============================

        roll_label = tk.Label(
            personal_card,
            text="Roll Number",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        roll_label.pack(
            anchor="w",
            padx=25
        )


        self.roll_entry = tk.Entry(
            personal_card,
            font=("Arial", 11),
            bg="#f1f5f9",
            fg=self.secondary_text,
            relief="solid",
            bd=1,
            state="readonly"
        )

        self.roll_entry.pack(
            fill="x",
            padx=25,
            pady=(5, 15),
            ipady=7
        )

        self.roll_entry.config(
            state="normal"
        )

        self.roll_entry.insert(
            0,
            str(student["roll_no"])
        )

        self.roll_entry.config(
            state="readonly"
        )


        # ==============================
        # Age
        # ==============================

        age_label = tk.Label(
            personal_card,
            text="Age",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        age_label.pack(
            anchor="w",
            padx=25
        )


        self.age_entry = tk.Entry(
            personal_card,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.age_entry.pack(
            fill="x",
            padx=25,
            pady=(5, 15),
            ipady=7
        )

        self.age_entry.insert(
            0,
            str(student["age"])
        )


        # ==============================
        # Course
        # ==============================

        course_label = tk.Label(
            personal_card,
            text="Course",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        course_label.pack(
            anchor="w",
            padx=25
        )


        self.course_var = tk.StringVar()

        self.course_menu = tk.OptionMenu(
            personal_card,
            self.course_var,
            *courses.keys(),
            command=self.course_selected
        )

        self.course_menu.config(
            font=("Arial", 11),
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black",
            highlightthickness=0
        )

        self.course_menu["menu"].config(
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black"
        )

        self.course_menu.pack(
            fill="x",
            padx=25,
            pady=(5, 15),
            ipady=5
        )

        self.course_var.set(
            student["course"]
        )


        # ==============================
        # Year
        # ==============================

        year_label = tk.Label(
            personal_card,
            text="Year",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        year_label.pack(
            anchor="w",
            padx=25
        )


        self.year_var = tk.StringVar()

        self.year_menu = tk.OptionMenu(
            personal_card,
            self.year_var,
            "Select Year"
        )

        self.year_menu.config(
            font=("Arial", 11),
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black",
            highlightthickness=0
        )

        self.year_menu["menu"].config(
            bg="white",
            fg="black",
            activebackground="#e2e8f0",
            activeforeground="black"
        )

        self.year_menu.pack(
            fill="x",
            padx=25,
            pady=(5, 25),
            ipady=5
        )


        self.load_years(
            student["course"],
            student["year"]
        )


        # ==============================
        # Subjects & Marks
        # ==============================

        subjects_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        subjects_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        subjects_title = tk.Label(
            subjects_card,
            text="Subjects & Marks",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        subjects_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        self.subjects_frame = tk.Frame(
            subjects_card,
            bg=self.card_color
        )

        self.subjects_frame.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )


        # ==============================
        # Load Existing Subjects
        # ==============================

        subjects = courses[
            student["course"]
        ][
            student["year"]
        ]


        self.show_subjects(
            subjects,
            student["marks"]
        )


        # ==============================
        # Button Container
        # ==============================

        button_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        button_frame.pack(
            fill="x",
            padx=40,
            pady=(0, 40)
        )


        # ==============================
        # Back Button
        # ==============================

        back_button = tk.Label(
            button_frame,
            text="← Back",
            font=("Arial", 11, "bold"),
            bg="#e2e8f0",
            fg=self.text_color,
            cursor="hand2",
            padx=25,
            pady=10
        )

        back_button.pack(
            side="left"
        )


        back_button.bind(
            "<Button-1>",
            lambda event: self.back_callback()
        )


        back_button.bind(
            "<Enter>",
            lambda event: back_button.config(
                bg="#cbd5e1"
            )
        )

        back_button.bind(
            "<Leave>",
            lambda event: back_button.config(
                bg="#e2e8f0"
            )
        )


        # ==============================
        # Update Student Button
        # ==============================

        update_button = tk.Label(
            button_frame,
            text="Update Student",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white",
            cursor="hand2",
            padx=25,
            pady=10
        )

        update_button.pack(
            side="right"
        )


        update_button.bind(
            "<Button-1>",
            lambda event: self.validate_student()
        )


        update_button.bind(
            "<Enter>",
            lambda event: update_button.config(
                bg="#334155"
            )
        )

        update_button.bind(
            "<Leave>",
            lambda event: update_button.config(
                bg="#1e293b"
            )
        )


    # ==============================
    # Load Years
    # ==============================

    def load_years(
        self,
        selected_course,
        selected_year
    ):

        menu = self.year_menu["menu"]

        menu.delete(
            0,
            "end"
        )


        for year in courses[selected_course].keys():

            menu.add_command(
                label=year,
                command=lambda value=year:
                    self.year_selected(value)
            )


        self.year_var.set(
            selected_year
        )


    # ==============================
    # Course Selected
    # ==============================

    def course_selected(
        self,
        selected_course
    ):

        self.year_var.set(
            "Select Year"
        )


        menu = self.year_menu["menu"]

        menu.delete(
            0,
            "end"
        )


        for year in courses[selected_course].keys():

            menu.add_command(
                label=year,
                command=lambda value=year:
                    self.year_selected(value)
            )


        self.clear_subjects()


    # ==============================
    # Year Selected
    # ==============================

    def year_selected(
        self,
        selected_year
    ):

        self.year_var.set(
            selected_year
        )


        course = self.course_var.get()


        if course in courses:

            subjects = courses[
                course
            ][
                selected_year
            ]


            self.show_subjects(
                subjects,
                {}
            )


    # ==============================
    # Show Subjects
    # ==============================

    def show_subjects(
        self,
        subjects,
        existing_marks
    ):

        self.clear_subjects()

        self.subject_entries = {}


        for subject in subjects:

            subject_frame = tk.Frame(
                self.subjects_frame,
                bg=self.card_color
            )

            subject_frame.pack(
                fill="x",
                pady=6
            )


            subject_label = tk.Label(
                subject_frame,
                text=subject,
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.text_color,
                anchor="w"
            )

            subject_label.pack(
                side="left",
                fill="x",
                expand=True
            )


            marks_entry = tk.Entry(
                subject_frame,
                font=("Arial", 11),
                width=10,
                bg="white",
                fg="black",
                insertbackground="black",
                relief="solid",
                bd=1
            )

            marks_entry.pack(
                side="right",
                ipady=5
            )


            if subject in existing_marks:

                marks_entry.insert(
                    0,
                    str(existing_marks[subject])
                )


            self.subject_entries[
                subject
            ] = marks_entry


    # ==============================
    # Clear Subjects
    # ==============================

    def clear_subjects(self):

        for widget in self.subjects_frame.winfo_children():

            widget.destroy()


    # ==============================
    # Validate Student
    # ==============================

    def validate_student(self):

        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        course = self.course_var.get()
        year = self.year_var.get()


        # ==============================
        # Name Validation
        # ==============================

        if not name:

            messagebox.showerror(
                "Invalid Name",
                "Please enter the student's name."
            )

            return


        if not all(
            character.isalpha() or character.isspace()
            for character in name
        ):

            messagebox.showerror(
                "Invalid Name",
                "Name should contain only letters and spaces."
            )

            return


        # ==============================
        # Age Validation
        # ==============================

        if not age:

            messagebox.showerror(
                "Invalid Age",
                "Please enter the student's age."
            )

            return


        if not age.isdigit():

            messagebox.showerror(
                "Invalid Age",
                "Age should contain only digits."
            )

            return


        age_value = int(age)


        if age_value < 15 or age_value > 60:

            messagebox.showerror(
                "Invalid Age",
                "Age must be between 15 and 60."
            )

            return


        # ==============================
        # Course Validation
        # ==============================

        if course not in courses:

            messagebox.showerror(
                "Invalid Course",
                "Please select a course."
            )

            return


        # ==============================
        # Year Validation
        # ==============================

        if year not in courses[course]:

            messagebox.showerror(
                "Invalid Year",
                "Please select a valid year."
            )

            return


        # ==============================
        # Marks Validation
        # ==============================

        if not self.subject_entries:

            messagebox.showerror(
                "Subjects Missing",
                "Please select a course and year."
            )

            return


        marks = {}


        for subject, entry in self.subject_entries.items():

            mark = entry.get().strip()


            if not mark:

                messagebox.showerror(
                    "Invalid Marks",
                    f"Please enter marks for {subject}."
                )

                return


            if not mark.isdigit():

                messagebox.showerror(
                    "Invalid Marks",
                    f"Marks for {subject} should contain only digits."
                )

                return


            mark_value = int(mark)


            if mark_value < 0 or mark_value > 100:

                messagebox.showerror(
                    "Invalid Marks",
                    f"Marks for {subject} must be between 0 and 100."
                )

                return


            marks[subject] = mark_value


        # ==============================
        # Prepare Updated Student
        # ==============================

        student = {

            "name": name,

            "roll_no": self.original_roll_no,

            "course": course,

            "year": year,

            "age": age_value,

            "marks": marks
        }


        # ==============================
        # Update Student in SQLite
        # ==============================

        try:

            updated = update_student(
                student
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Student could not be updated.\n\n{error}"
            )

            return


        if not updated:

            messagebox.showerror(
                "Update Failed",
                "Student could not be found."
            )

            return


        # ==============================
        # Success Message
        # ==============================

        messagebox.showinfo(
            "Student Updated",
            "Student has been updated successfully."
        )


        # ==============================
        # Show Updated Page
        # ==============================

        self.show(
            self.original_roll_no
        )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()