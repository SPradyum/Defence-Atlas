# main.py

import tkinter as tk
from PIL import Image, ImageTk
from data_store import DEFENCE_DATA, DASHBOARD_BG

COLORS = {
    "Army": "#556B2F",
    "Air Force": "#1E90FF",
    "Navy": "#0B3C5D",
    "NCC": "#800000"
}


class DefenceAtlas:
    def __init__(self, root):
        self.root = root
        self.root.title("Indian Defence Atlas")
        self.root.state("zoomed")

        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.widgets = []
        self.images = []
        self.content_items = []

        self.root.after(100, self.show_dashboard)

    # ---------- CLEAN ----------
    def clear(self):
        self.canvas.delete("all")
        for w in self.widgets:
            w.destroy()
        self.widgets.clear()
        self.images.clear()
        self.content_items.clear()

    # ---------- BACKGROUND ----------
    def draw_background(self, image_path):
        self.root.update_idletasks()
        w, h = self.root.winfo_width(), self.root.winfo_height()

        img = Image.open(image_path)
        img_ratio = img.width / img.height
        win_ratio = w / h

        if win_ratio > img_ratio:
            new_h = h
            new_w = int(h * img_ratio)
        else:
            new_w = w
            new_h = int(w / img_ratio)

        img = img.resize((new_w, new_h), Image.LANCZOS)
        bg = ImageTk.PhotoImage(img)
        self.images.append(bg)

        self.canvas.create_image(w // 2, h // 2, image=bg, anchor="center")

    # ---------- DASHBOARD ----------
    def show_dashboard(self):
        self.clear()
        self.draw_background(DASHBOARD_BG)

        w, h = self.root.winfo_width(), self.root.winfo_height()

        self.canvas.create_text(
            w // 2, 70,
            text="INDIAN DEFENCE ATLAS",
            fill="#FF9933",
            font=("Arial", 34, "bold")
        )

        self.canvas.create_text(
            w // 2, 115,
            text="Explore the Strength of India's Armed Forces",
            fill="white",
            font=("Arial", 14)
        )

        self.canvas.create_rectangle(
            w // 2 - 220, h // 2 - 180,
            w // 2 + 220, h // 2 + 180,
            fill="#000000",
            stipple="gray25",
            outline=""
        )

        y = h // 2 - 110
        for force in DEFENCE_DATA:
            btn = tk.Button(
                self.root,
                text=force,
                width=24,
                height=2,
                font=("Arial", 12, "bold"),
                bg=COLORS[force],
                fg="white",
                relief="flat",
                cursor="hand2",
                command=lambda f=force: self.show_force_ui(f)
            )
            self.canvas.create_window(w // 2, y, window=btn)
            self.widgets.append(btn)
            y += 60

    # ---------- FORCE UI ----------
    def show_force_ui(self, force):
        self.clear()
        self.force = force
        self.data = DEFENCE_DATA[force]

        self.draw_background(self.data["bg_image"])
        w, h = self.root.winfo_width(), self.root.winfo_height()

        # Header
        self.canvas.create_rectangle(0, 0, w, 90, fill=COLORS[force], outline="")

        try:
            logo = ImageTk.PhotoImage(
                Image.open(self.data["logo"]).resize((56, 56), Image.LANCZOS)
            )
            self.images.append(logo)
            self.canvas.create_image(30, 45, image=logo, anchor="w")
        except:
            pass

        self.canvas.create_text(
            100, 45,
            text=f"INDIAN {force.upper()}",
            fill="white",
            font=("Arial", 26, "bold"),
            anchor="w"
        )

        # Content panel
        self.panel_left = int(w * 0.32)
        self.panel_top = 130
        self.panel_right = w - 80
        self.panel_bottom = h - 90

        self.panel_id = self.canvas.create_rectangle(
            self.panel_left, self.panel_top,
            self.panel_right, self.panel_bottom,
            fill="#000000",
            stipple="gray25",
            outline=""
        )

        # Tabs
        tabs = [
            ("About", "about"),
            ("Motto", "motto"),
            ("Commands", "commands"),
            ("Ranks", "ranks"),
            ("Equipment", "equipment"),
        ]

        tab_y = self.panel_top + 30
        for label, key in tabs:
            b = tk.Button(
                self.root,
                text=label,
                width=16,
                font=("Arial", 11, "bold"),
                bg=COLORS[force],
                fg="white",
                relief="flat",
                cursor="hand2",
                command=lambda k=key: self.show_tab(k)
            )
            self.canvas.create_window(140, tab_y, window=b)
            self.widgets.append(b)
            tab_y += 48

        # Back
        back = tk.Button(
            self.root,
            text="⬅ Back to Dashboard",
            bg="#2A2A2A",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            command=self.show_dashboard
        )
        self.canvas.create_window(w // 2, h - 45, window=back)
        self.widgets.append(back)

        self.show_tab("about")

    # ---------- TAB CONTENT (FINAL & SAFE) ----------
    def show_tab(self, key):
        for item in self.content_items:
            self.canvas.delete(item)
        self.content_items.clear()

        padding = 50
        x = self.panel_left + padding
        y = self.panel_top + 40
        width = self.panel_right - self.panel_left - padding * 2

        title_text = key.upper()
        body_text = self.data.get(key, "Information not available.")

        title_id = self.canvas.create_text(
            x, y,
            text=title_text,
            fill="#FFD700",
            font=("Arial", 18, "bold"),
            anchor="nw"
        )

        body_id = self.canvas.create_text(
            x, y + 42,
            text=body_text,
            fill="#F2F2F2",
            font=("Arial", 14),
            anchor="nw",
            width=width
        )

        self.canvas.tag_raise(title_id, self.panel_id)
        self.canvas.tag_raise(body_id, self.panel_id)

        self.content_items.extend([title_id, body_id])


if __name__ == "__main__":
    root = tk.Tk()
    DefenceAtlas(root)
    root.mainloop()
