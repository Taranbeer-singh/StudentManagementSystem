import tkinter as tk


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
        self.text_color = "#0f172a"


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
        # Navigation
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
        # Settings
        # ==============================

        settings_frame = tk.Frame(
            self.sidebar,
            bg=self.sidebar_color
        )

        settings_frame.pack(
            fill="x",
            pady=(0, 20)
        )


        self.create_navigation_button(
            settings_frame,
            "⚙️  Settings",
            self.show_settings
        )


        # ==============================
        # Initial Page
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
        # Click
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
        # Hover
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
    # Dashboard Page
    # ==============================

    def show_dashboard(self):

        self.clear_content()

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
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
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
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.content,
            text="Manage and view all registered students",
            font=("Arial", 12),
            bg=self.background_color,
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
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
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.content,
            text="Add a new student to the system",
            font=("Arial", 12),
            bg=self.background_color,
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
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
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.content,
            text="Search students using their roll number",
            font=("Arial", 12),
            bg=self.background_color,
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
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
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.content,
            text="View student performance statistics",
            font=("Arial", 12),
            bg=self.background_color,
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
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
            pady=(35, 5)
        )


        subtitle = tk.Label(
            self.content,
            text="Application settings",
            font=("Arial", 12),
            bg=self.background_color,
            fg="#64748b"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
        )


# ==============================
# Start Application
# ==============================

if __name__ == "__main__":

    root = tk.Tk()

    app = DashboardApp(root)

    root.mainloop()