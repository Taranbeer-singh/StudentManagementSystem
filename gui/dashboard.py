import tkinter as tk

from gui.dashboard_page import DashboardPage
from gui.students_page import StudentsPage
from gui.settings_page import SettingsPage
from gui.add_student_page import AddStudentPage
from gui.search_page import SearchPage

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


        # Set root background

        self.root.configure(
            bg=self.background_color
        )


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


        # ==============================
        # Content Area
        # ==============================

        self.content_area = tk.Frame(
            self.root,
            bg=self.background_color
        )

        self.content_area.pack(
            side="right",
            fill="both",
            expand=True
        )


        # ==============================
        # Scrollable Canvas
        # ==============================

        self.canvas = tk.Canvas(
            self.content_area,
            bg=self.background_color,
            highlightthickness=0,
            bd=0
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        # ==============================
        # Scrollbar
        # ==============================

        self.scrollbar = tk.Scrollbar(
            self.content_area,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )


        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )


        # ==============================
        # Scrollable Content Frame
        # ==============================

        self.content = tk.Frame(
            self.canvas,
            bg=self.background_color
        )


        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.content,
            anchor="nw"
        )


        # ==============================
        # Scroll Region
        # ==============================

        self.content.bind(
            "<Configure>",
            self.update_scroll_region
        )


        self.canvas.bind(
            "<Configure>",
            self.resize_content_width
        )


        # ==============================
        # Mouse Wheel
        # ==============================

        self.canvas.bind(
            "<MouseWheel>",
            self.mouse_wheel
        )


        self.content.bind(
            "<MouseWheel>",
            self.mouse_wheel
        )


        # ==============================
        # Keyboard Scrolling
        # ==============================

        self.root.bind(
            "<Up>",
            self.keyboard_scroll_up
        )

        self.root.bind(
            "<Down>",
            self.keyboard_scroll_down
        )

        self.root.bind(
            "<Prior>",
            self.keyboard_page_up
        )

        self.root.bind(
            "<Next>",
            self.keyboard_page_down
        )

        self.root.bind(
            "<Home>",
            self.keyboard_home
        )

        self.root.bind(
            "<End>",
            self.keyboard_end
        )


        # ==============================
        # Page Objects
        # ==============================

        self.dashboard_page = DashboardPage(
            self.content,
            self.background_color,
            self.card_color,
            self.text_color,
            self.secondary_text
        )


        self.students_page = StudentsPage(
            self.content,
            self.background_color,
            self.card_color,
            self.text_color,
            self.secondary_text
        )


        self.settings_page = SettingsPage(
            self.content,
            self.background_color,
            self.card_color,
            self.text_color,
            self.secondary_text
        )

        self.search_page = SearchPage(
            self.content,
            self.background_color,
            self.card_color,
            self.text_color,
            self.secondary_text
        )

        self.add_student_page = AddStudentPage(
            self.content,
            self.background_color,
            self.card_color,
            self.text_color,
            self.secondary_text
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
    # Update Scroll Region
    # ==============================

    def update_scroll_region(self, event=None):

        self.content.update_idletasks()

        bbox = self.canvas.bbox(
            "all"
        )

        if bbox:

            self.canvas.configure(
                scrollregion=bbox
            )

        else:

            self.canvas.configure(
                scrollregion=(0, 0, 0, 0)
            )


    # ==============================
    # Resize Content Width
    # ==============================

    def resize_content_width(self, event):

        self.canvas.itemconfigure(
            self.canvas_window,
            width=event.width
        )

        self.root.after_idle(
            self.update_scroll_region
        )


    # ==============================
    # Mouse Wheel
    # ==============================

    def mouse_wheel(self, event):

        if event.delta:

            self.canvas.yview_scroll(
                int(-event.delta / 3),
                "units"
            )

        return "break"


    # ==============================
    # Keyboard - Up
    # ==============================

    def keyboard_scroll_up(self, event):

        self.canvas.yview_scroll(
            -1,
            "units"
        )

        return "break"


    # ==============================
    # Keyboard - Down
    # ==============================

    def keyboard_scroll_down(self, event):

        self.canvas.yview_scroll(
            1,
            "units"
        )

        return "break"


    # ==============================
    # Keyboard - Page Up
    # ==============================

    def keyboard_page_up(self, event):

        self.canvas.yview_scroll(
            -5,
            "units"
        )

        return "break"


    # ==============================
    # Keyboard - Page Down
    # ==============================

    def keyboard_page_down(self, event):

        self.canvas.yview_scroll(
            5,
            "units"
        )

        return "break"


    # ==============================
    # Keyboard - Home
    # ==============================

    def keyboard_home(self, event):

        self.canvas.yview_moveto(
            0
        )

        return "break"


    # ==============================
    # Keyboard - End
    # ==============================

    def keyboard_end(self, event):

        self.canvas.yview_moveto(
            1
        )

        return "break"


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
    # Dashboard
    # ==============================

    def show_dashboard(self):

        self.dashboard_page.show()

        self.reset_scroll()


    # ==============================
    # Students
    # ==============================

    def show_students(self):

        self.students_page.show()

        self.reset_scroll()


    # ==============================
    # Add Student
    # ==============================

    def show_add_student(self):

        self.add_student_page.show()

        self.reset_scroll()


    # ==============================
    # Search
    # ==============================

    def show_search(self):

        self.search_page.show()
        
        self.reset_scroll()


    # ==============================
    # Statistics
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
            fg=self.secondary_text
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 25)
        )


        self.reset_scroll()


    # ==============================
    # Settings
    # ==============================

    def show_settings(self):

        self.settings_page.show()

        self.reset_scroll()


    # ==============================
    # Reset Scroll
    # ==============================

    def reset_scroll(self):

        self.root.after_idle(
            self._reset_scroll
        )


    def _reset_scroll(self):

        self.content.update_idletasks()

        self.update_scroll_region()

        self.canvas.yview_moveto(
            0
        )


        self.canvas.update_idletasks()


    # ==============================
    # Clear Content
    # ==============================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

        self.reset_scroll()


# ==============================
# Start Application
# ==============================

if __name__ == "__main__":

    root = tk.Tk()

    app = DashboardApp(
        root
    )

    root.mainloop()