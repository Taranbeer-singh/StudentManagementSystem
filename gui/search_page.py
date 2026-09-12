import tkinter as tk
from tkinter import messagebox

from database import get_student_by_roll


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
            text="Search students using their roll number",
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


        # ==============================
        # Search Button Click
        # ==============================

        search_button.bind(
            "<Button-1>",
            lambda event: self.search_student()
        )


        # ==============================
        # Search Button Hover
        # ==============================

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


        result_card = tk.Frame(
            self.result_frame,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        result_card.pack(
            fill="x"
        )


        # ==============================
        # Result Heading
        # ==============================

        result_title = tk.Label(
            result_card,
            text="Student Found",
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
        # Student Information
        # ==============================

        self.create_info_row(
            result_card,
            "Name",
            student["name"]
        )


        self.create_info_row(
            result_card,
            "Roll Number",
            student["roll_no"]
        )


        self.create_info_row(
            result_card,
            "Course",
            student["course"]
        )


        self.create_info_row(
            result_card,
            "Year",
            student["year"]
        )


        self.create_info_row(
            result_card,
            "Age",
            student["age"]
        )


        # ==============================
        # Basic Result Note
        # ==============================

        note = tk.Label(
            result_card,
            text="Detailed marks and actions will be added in the next block.",
            font=("Arial", 10),
            bg=self.card_color,
            fg=self.secondary_text
        )

        note.pack(
            anchor="w",
            padx=25,
            pady=(10, 20)
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