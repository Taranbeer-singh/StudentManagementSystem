import tkinter as tk
from tkinter import messagebox


class SettingsPage:

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
    # Show Settings Page
    # ==============================

    def show(self):

        self.clear_page()


        # ==============================
        # Page Header
        # ==============================

        heading = tk.Label(
            self.parent,
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
            self.parent,
            text="Manage application preferences and information",
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
        # Application Information
        # ==============================

        self.create_section_title(
            "Application Information"
        )


        info_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        info_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        self.create_info_row(
            info_card,
            "Application",
            "Student Management System"
        )


        self.create_info_row(
            info_card,
            "Version",
            "1.0"
        )


        self.create_info_row(
            info_card,
            "Database",
            "SQLite"
        )


        self.create_info_row(
            info_card,
            "Platform",
            "Desktop Application"
        )


        # ==============================
        # Display Settings
        # ==============================

        self.create_section_title(
            "Display"
        )


        display_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        display_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        self.create_action_row(
            display_card,
            "Reset Window Size",
            "Restore the application window to its default size.",
            self.reset_window_size
        )


        self.create_action_row(
            display_card,
            "Reset Scroll Position",
            "Return the current page to the top.",
            self.reset_scroll_position
        )


        # ==============================
        # Data Settings
        # ==============================

        self.create_section_title(
            "Data"
        )


        data_card = tk.Frame(
            self.parent,
            bg=self.card_color,
            highlightthickness=1,
            highlightbackground="#e2e8f0"
        )

        data_card.pack(
            fill="x",
            padx=40,
            pady=(0, 25)
        )


        self.create_action_row(
            data_card,
            "Refresh Application Data",
            "Reload information from the database.",
            self.refresh_data
        )


    # ==============================
    # Section Title
    # ==============================

    def create_section_title(self, title):

        label = tk.Label(
            self.parent,
            text=title,
            font=("Arial", 18, "bold"),
            bg=self.background_color,
            fg=self.text_color
        )

        label.pack(
            anchor="w",
            padx=40,
            pady=(5, 12)
        )


    # ==============================
    # Information Row
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
            padx=20,
            pady=13
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
    # Action Row
    # ==============================

    def create_action_row(
        self,
        parent,
        title,
        description,
        command
    ):

        row = tk.Frame(
            parent,
            bg=self.card_color
        )

        row.pack(
            fill="x",
            padx=20,
            pady=13
        )


        text_frame = tk.Frame(
            row,
            bg=self.card_color
        )

        text_frame.pack(
            side="left",
            fill="x",
            expand=True
        )


        title_label = tk.Label(
            text_frame,
            text=title,
            font=("Arial", 11, "bold"),
            bg=self.card_color,
            fg=self.text_color,
            anchor="w"
        )

        title_label.pack(
            anchor="w"
        )


        description_label = tk.Label(
            text_frame,
            text=description,
            font=("Arial", 10),
            bg=self.card_color,
            fg=self.secondary_text,
            anchor="w"
        )

        description_label.pack(
            anchor="w",
            pady=(3, 0)
        )


        button = tk.Button(
            row,
            text="Run",
            font=("Arial", 10, "bold"),
            bg="#e2e8f0",
            fg=self.text_color,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=6,
            command=command
        )

        button.pack(
            side="right",
            padx=(15, 0)
        )


    # ==============================
    # Reset Window Size
    # ==============================

    def reset_window_size(self):

        root = self.parent.winfo_toplevel()

        root.geometry(
            "1100x700"
        )

        root.update_idletasks()

        if hasattr(root, "canvas"):

            root.canvas.yview_moveto(
                0
            )

            root.canvas.configure(
                scrollregion=root.canvas.bbox("all")
            )

            root.canvas.update_idletasks()


    # ==============================
    # Reset Scroll Position
    # ==============================

    def reset_scroll_position(self):

        root = self.parent.winfo_toplevel()

        if hasattr(root, "canvas"):

            root.canvas.yview_moveto(
                0
            )

            root.canvas.update_idletasks()


    # ==============================
    # Refresh Data
    # ==============================

    def refresh_data(self):

        messagebox.showinfo(
            "Data Refresh",
            "Application data will be refreshed when you open a page."
        )


    # ==============================
    # Clear Page
    # ==============================

    def clear_page(self):

        for widget in self.parent.winfo_children():

            widget.destroy()