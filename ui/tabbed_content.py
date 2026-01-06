# ui/tabbed_content.py
import tkinter as tk

class TabbedContent:
    def __init__(self, parent, color):
        self.color = color
        self.frames = {}
        self.buttons = {}

        self.bar = tk.Frame(parent, bg="#f0f0f0")
        self.bar.pack(fill="x")

        self.body = tk.Frame(parent, bg="white", padx=20, pady=20)
        self.body.pack(fill="both", expand=True)

    def add_tab(self, name, text):
        btn = tk.Button(
            self.bar, text=name.upper(), font=("Segoe UI", 10, "bold"),
            bd=0, cursor="hand2", padx=20, pady=10, relief="flat",
            command=lambda n=name: self.show(n)
        )
        btn.pack(side="left", padx=1)
        self.buttons[name] = btn

        frame = tk.Frame(self.body, bg="white")
        tk.Label(
            frame, text=text, font=("Segoe UI", 12),
            wraplength=600, justify="left", bg="white", fg="#2c3e50"
        ).pack(anchor="nw")

        self.frames[name] = frame
        if len(self.frames) == 1: self.show(name)

    def show(self, name):
        for f in self.frames.values(): f.pack_forget()
        self.frames[name].pack(fill="both", expand=True)
        for n, b in self.buttons.items():
            if n == name:
                b.config(bg=self.color, fg="white")
            else:
                b.config(bg="#e0e0e0", fg="#555555")