# ui/layout_manager.py
from PIL import Image, ImageTk, ImageEnhance

class BackgroundManager:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.image_path = None
        self.bg_img = None
        self.root.bind("<Configure>", self._redraw)

    def set_background(self, path):
        self.image_path = path
        self._redraw()

    def _redraw(self, event=None):
        if not self.image_path: return
        w, h = self.root.winfo_width(), self.root.winfo_height()
        if w < 50 or h < 50: return

        try:
            img = Image.open(self.image_path).resize((w, h), Image.Resampling.LANCZOS)
            # Darken background to make UI pop
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.6) 
            self.bg_img = ImageTk.PhotoImage(img)
            self.canvas.delete("bg")
            self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw", tags="bg")
            self.canvas.tag_lower("bg")
        except Exception as e:
            print(f"Error loading background: {e}")