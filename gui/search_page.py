import tkinter as tk
from tkinter import messagebox

from database import get_student_by_roll, delete_student
from statistics import get_student_marks_statistics


class SearchPage:

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
    # Show Search Page
    # ==============================

    def show(self):

        self.clear_page()


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Search Student",
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
            text="Search and manage students using their roll number",
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
        # Search Card
        # ==============================

        search_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        search_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        # ==============================
        # Search Title
        # ==============================

        search_title = tk.Label(
            search_card,
            text="Find Student",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        search_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Roll Number Label
        # ==============================

        roll_label = tk.Label(
            search_card,
            text="Roll Number",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        roll_label.pack(
            anchor="w",
            padx=25
        )


        # ==============================
        # Search Input Container
        # ==============================

        input_frame = tk.Frame(
            search_card,
            bg=self.card_color
        )

        input_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 25)
        )


        # ==============================
        # Roll Number Entry
        # ==============================

        self.roll_entry = tk.Entry(
            input_frame,
            font=("Arial", 11),
            bg="white",
            fg="black",
            insertbackground="black",
            relief="solid",
            bd=1
        )

        self.roll_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8
        )


        # ==============================
        # Search Button
        # ==============================

        search_button = tk.Label(
            input_frame,
            text="🔍  Search",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white",
            cursor="hand2",
            padx=22,
            pady=9
        )

        search_button.pack(
            side="left",
            padx=(10, 0)
        )


        search_button.bind(
            "<Button-1>",
            lambda event: self.search_student()
        )


        search_button.bind(
            "<Enter>",
            lambda event: search_button.config(
                bg="#334155"
            )
        )


        search_button.bind(
            "<Leave>",
            lambda event: search_button.config(
                bg="#1e293b"
            )
        )


        # ==============================
        # Enter Key Search
        # ==============================

        self.roll_entry.bind(
            "<Return>",
            lambda event: self.search_student()
        )


        # ==============================
        # Result Area
        # ==============================

        self.result_frame = tk.Frame(
            self.parent,
            bg=self.background_color
        )

        self.result_frame.pack(
            fill="x",
            padx=40
        )


        # ==============================
        # Initial Message
        # ==============================

        self.show_initial_message()


    # ==============================
    # Search Student
    # ==============================

    def search_student(self):

        roll_no = self.roll_entry.get().strip()


        # ==============================
        # Empty Roll Number
        # ==============================

        if not roll_no:

            messagebox.showerror(
                "Invalid Roll Number",
                "Please enter a roll number."
            )

            return


        # ==============================
        # Roll Number Validation
        # ==============================

        if not roll_no.isdigit():

            messagebox.showerror(
                "Invalid Roll Number",
                "Roll number should contain only digits."
            )

            return


        roll_no = int(roll_no)


        # ==============================
        # Search Database
        # ==============================

        student = get_student_by_roll(
            roll_no
        )


        # ==============================
        # Student Not Found
        # ==============================

        if student is None:

            self.show_not_found()

            return


        # ==============================
        # Show Student
        # ==============================

        self.show_student(
            student
        )


    # ==============================
    # Show Student
    # ==============================

    def show_student(self, student):

        self.clear_result()


        # ==============================
        # Calculate Marks Statistics
        # ==============================

        total_marks, obtained_marks, percentage = (
            get_student_marks_statistics(
                student
            )
        )


        # ==============================
        # Student Information Card
        # ==============================

        info_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        info_card.pack(
            fill="x",
            pady=(0, 20)
        )


        # ==============================
        # Card Heading
        # ==============================

        result_title = tk.Label(
            info_card,
            text="Student Information",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        result_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Student Information Rows
        # ==============================

        self.create_info_row(
            info_card,
            "Name",
            student["name"]
        )


        self.create_info_row(
            info_card,
            "Roll Number",
            student["roll_no"]
        )


        self.create_info_row(
            info_card,
            "Course",
            student["course"]
        )


        self.create_info_row(
            info_card,
            "Year",
            student["year"]
        )


        self.create_info_row(
            info_card,
            "Age",
            student["age"]
        )


        # ==============================
        # Performance Card
        # ==============================

        performance_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        performance_card.pack(
            fill="x",
            pady=(0, 20)
        )


        performance_title = tk.Label(
            performance_card,
            text="Academic Performance",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        performance_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Performance Statistics
        # ==============================

        statistics_frame = tk.Frame(
            performance_card,
            bg=self.card_color
        )

        statistics_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )


        self.create_performance_card(
            statistics_frame,
            "Total Marks",
            total_marks
        )


        self.create_performance_card(
            statistics_frame,
            "Obtained Marks",
            obtained_marks
        )


        self.create_performance_card(
            statistics_frame,
            "Percentage",
            f"{percentage:.2f}%"
        )


        # ==============================
        # Subjects & Marks Card
        # ==============================

        marks_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        marks_card.pack(
            fill="x",
            pady=(0, 20)
        )


        marks_title = tk.Label(
            marks_card,
            text="Subjects & Marks",
            font=("Arial", 18, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        marks_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15)
        )


        # ==============================
        # Subject Rows
        # ==============================

        for subject, marks in student["marks"].items():

            self.create_marks_row(
                marks_card,
                subject,
                marks
            )


        # ==============================
        # Action Buttons
        # ==============================

        action_frame = tk.Frame(
            self.result_frame,
            bg=self.background_color
        )

        action_frame.pack(
            fill="x",
            pady=(0, 40)
        )


        # ==============================
        # New Search Button
        # ==============================

        new_search_button = tk.Label(
            action_frame,
            text="🔄  New Search",
            font=("Arial", 11, "bold"),
            bg="#e2e8f0",
            fg=self.text_color,
            cursor="hand2",
            padx=20,
            pady=10
        )

        new_search_button.pack(
            side="left"
        )


        new_search_button.bind(
            "<Button-1>",
            lambda event: self.new_search()
        )


        new_search_button.bind(
            "<Enter>",
            lambda event: new_search_button.config(
                bg="#cbd5e1"
            )
        )


        new_search_button.bind(
            "<Leave>",
            lambda event: new_search_button.config(
                bg="#e2e8f0"
            )
        )


        # ==============================
        # Edit Button
        # ==============================

        edit_button = tk.Label(
            action_frame,
            text="✏️  Edit",
            font=("Arial", 11, "bold"),
            bg="#e2e8f0",
            fg=self.text_color,
            cursor="hand2",
            padx=20,
            pady=10
        )

        edit_button.pack(
            side="right",
            padx=(10, 0)
        )


        edit_button.bind(
            "<Button-1>",
            lambda event: self.edit_student(
                student["roll_no"]
            )
        )


        edit_button.bind(
            "<Enter>",
            lambda event: edit_button.config(
                bg="#cbd5e1"
            )
        )


        edit_button.bind(
            "<Leave>",
            lambda event: edit_button.config(
                bg="#e2e8f0"
            )
        )


        # ==============================
        # Delete Button
        # ==============================

        delete_button = tk.Label(
            action_frame,
            text="🗑️  Delete",
            font=("Arial", 11, "bold"),
            bg="#fee2e2",
            fg="#991b1b",
            cursor="hand2",
            padx=20,
            pady=10
        )

        delete_button.pack(
            side="right"
        )


        delete_button.bind(
            "<Button-1>",
            lambda event: self.delete_student(
                student["roll_no"]
            )
        )


        delete_button.bind(
            "<Enter>",
            lambda event: delete_button.config(
                bg="#fecaca"
            )
        )


        delete_button.bind(
            "<Leave>",
            lambda event: delete_button.config(
                bg="#fee2e2"
            )
        )


    # ==============================
    # Create Information Row
    # ==============================

    def create_info_row(
        self,
        parent,
        title,
        value
    ):

        row = tk.Frame(
            parent,
            bg=self.card_color
        )

        row.pack(
            fill="x",
            padx=25,
            pady=7
        )


        title_label = tk.Label(
            row,
            text=title,
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color,
            anchor="w"
        )

        title_label.pack(
            side="left"
        )


        value_label = tk.Label(
            row,
            text=value,
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text,
            anchor="e"
        )

        value_label.pack(
            side="right"
        )


    # ==============================
    # Performance Card
    # ==============================

    def create_performance_card(
        self,
        parent,
        title,
        value
    ):

        card = tk.Frame(
            parent,
            bg="#f8fafc",
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
            font=("Arial", 10),
            bg="#f8fafc",
            fg=self.secondary_text
        )

        title_label.pack(
            pady=(15, 3)
        )


        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 18, "bold"),
            bg="#f8fafc",
            fg=self.text_color
        )

        value_label.pack(
            pady=(0, 15)
        )


    # ==============================
    # Create Marks Row
    # ==============================

    def create_marks_row(
        self,
        parent,
        subject,
        marks
    ):

        row = tk.Frame(
            parent,
            bg=self.card_color
        )

        row.pack(
            fill="x",
            padx=25,
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
            side="left",
            fill="x",
            expand=True
        )


        marks_label = tk.Label(
            row,
            text=f"{marks} / 100",
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color,
            anchor="e"
        )

        marks_label.pack(
            side="right"
        )


    # ==============================
    # New Search
    # ==============================

    def new_search(self):

        self.roll_entry.delete(
            0,
            "end"
        )

        self.show_initial_message()

        self.roll_entry.focus_set()


    # ==============================
    # Edit Student
    # ==============================

    def edit_student(self, roll_no):

        messagebox.showinfo(
            "Edit Student",
            f"Edit page for Roll No. {roll_no} will be connected next."
        )


    # ==============================
    # Delete Student
    # ==============================

    def delete_student(self, roll_no):

        confirmation = messagebox.askyesno(
            "Delete Student",
            f"Are you sure you want to delete student with Roll No. {roll_no}?"
        )


        if not confirmation:

            return


        deleted = delete_student(
            roll_no
        )


        if deleted:

            messagebox.showinfo(
                "Student Deleted",
                "Student has been deleted successfully."
            )

            self.new_search()

        else:

            messagebox.showerror(
                "Delete Error",
                "Student could not be deleted."
            )


    # ==============================
    # Show Initial Message
    # ==============================

    def show_initial_message(self):

        self.clear_result()


        initial_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        initial_card.pack(
            fill="x"
        )


        initial_label = tk.Label(
            initial_card,
            text="Enter a roll number to search for a student.",
            font=("Arial", 12),
            bg=self.card_color,
            fg=self.secondary_text
        )

        initial_label.pack(
            pady=25
        )


    # ==============================
    # Student Not Found
    # ==============================

    def show_not_found(self):

        self.clear_result()


        result_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        result_card.pack(
            fill="x"
        )


        icon = tk.Label(
            result_card,
            text="🔍",
            font=("Arial", 25),
            bg=self.card_color
        )

        icon.pack(
            pady=(20, 5)
        )


        title = tk.Label(
            result_card,
            text="Student Not Found",
            font=("Arial", 17, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )

        title.pack()


        message = tk.Label(
            result_card,
            text="No student was found with this roll number.",
            font=("Arial", 11),
            bg=self.card_color,
            fg=self.secondary_text
        )

        message.pack(
            pady=(5, 20)
        )


    # ==============================
    # Clear Result
    # ==============================

    def clear_result(self):

        for widget in self.result_frame.winfo_children():

            widget.destroy()


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()