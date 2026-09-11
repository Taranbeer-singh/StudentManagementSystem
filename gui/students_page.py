import tkinter as tk
from tkinter import messagebox

from database import get_all_students, delete_student
from statistics import get_student_marks_statistics


class StudentsPage:

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
    # Show Students Page
    # ==============================

    def show(self):

        self.clear_page()

        students = get_all_students()


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
            text="Students",
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
            text="Manage and view all registered students",
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
        # Table Container
        # ==============================

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
            "Percentage",
            "Actions"
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
                pady=14,
                sticky="w"
            )


        # ==============================
        # Student Data
        # ==============================

        if students:

            for row, student in enumerate(
                students,
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
                        pady=12,
                        sticky="w"
                    )


                # ==============================
                # Action Buttons
                # ==============================

                actions_frame = tk.Frame(
                    table_frame,
                    bg=self.card_color
                )

                actions_frame.grid(
                    row=row,
                    column=5,
                    padx=10,
                    pady=8
                )


                # Edit Button

                edit_button = tk.Button(
                    actions_frame,
                    text="✏️ Edit",
                    font=("Arial", 10),
                    bg="#e2e8f0",
                    fg=self.text_color,
                    relief="flat",
                    cursor="hand2",
                    padx=8,
                    pady=4,
                    command=lambda roll=student["roll_no"]:
                        self.edit_student(roll)
                )

                edit_button.pack(
                    side="left",
                    padx=3
                )


                # Delete Button

                delete_button = tk.Button(
                    actions_frame,
                    text="🗑️ Delete",
                    font=("Arial", 10),
                    bg="#fee2e2",
                    fg="#991b1b",
                    relief="flat",
                    cursor="hand2",
                    padx=8,
                    pady=4,
                    command=lambda roll=student["roll_no"]:
                        self.delete_student(roll)
                )

                delete_button.pack(
                    side="left",
                    padx=3
                )


        else:

            empty_label = tk.Label(
                table_frame,
                text="No students found.",
                font=("Arial", 12),
                bg=self.card_color,
                fg=self.secondary_text
            )

            empty_label.grid(
                row=1,
                column=0,
                columnspan=6,
                pady=25
            )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()


    # ==============================
    # Edit Student
    # ==============================

    def edit_student(self, roll_no):

        messagebox.showinfo(
            "Edit Student",
            f"Edit functionality for Roll No. {roll_no} will be connected next."
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

            self.show()

        else:

            messagebox.showerror(
                "Error",
                "Student could not be deleted."
            )