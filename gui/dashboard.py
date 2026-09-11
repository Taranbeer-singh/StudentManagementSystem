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
        # Main Layout
        # ==============================

        self.sidebar = tk.Frame(
            self.root,
            width=220
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(
            False
        )


        self.content = tk.Frame(
            self.root
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
            font=("Arial", 18, "bold")
        )

        title.pack(
            pady=(35, 45)
        )


        # ==============================
        # Navigation Buttons
        # ==============================

        self.create_navigation_button(
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.create_navigation_button(
            "👨‍🎓  Students",
            self.show_students
        )

        self.create_navigation_button(
            "➕  Add Student",
            self.show_add_student
        )

        self.create_navigation_button(
            "🔍  Search",
            self.show_search
        )

        self.create_navigation_button(
            "📊  Statistics",
            self.show_statistics
        )

        self.create_navigation_button(
            "⚙️  Settings",
            self.show_settings
        )


        # Show dashboard initially
        self.show_dashboard()


    # ==============================
    # Navigation Button
    # ==============================

    def create_navigation_button(
        self,
        text,
        command
    ):

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            font=("Arial", 12),
            anchor="w",
            padx=25,
            relief="flat",
            bd=0
        )

        button.pack(
            fill="x",
            ipady=12,
            padx=15,
            pady=3
        )


    # ==============================
    # Clear Content Area
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
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Welcome to Student Management System",
            font=("Arial", 16)
        )

        message.pack(
            anchor="w",
            padx=40
        )


    # ==============================
    # Students Page
    # ==============================

    def show_students(self):

        self.clear_content()

        heading = tk.Label(
            self.content,
            text="Students",
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Student list will appear here.",
            font=("Arial", 16)
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
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Add Student form will appear here.",
            font=("Arial", 16)
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
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Search functionality will appear here.",
            font=("Arial", 16)
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
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Statistics dashboard will appear here.",
            font=("Arial", 16)
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
            font=("Arial", 28, "bold")
        )

        heading.pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )


        message = tk.Label(
            self.content,
            text="Settings will appear here.",
            font=("Arial", 16)
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