import math
import tkinter as tk

# --- Configuration ---
WIDTH, HEIGHT = 800, 800
NUM_WORDS_PER_LINE = 50  # Words per layer
TEXT_SPACING = (2 * math.pi) / NUM_WORDS_PER_LINE
ANIMATION_SPEED = 0.015  # Speed of the flow

# Scale sizes for the three distinct lines (Outer, Middle, Inner)
SCALES = [19.5, 18.0, 16.5]


# --- Mathematical Heart Formula ---
def get_heart_coordinate(t, scale):
    # Standard parametric heart equations
    x = 16 * (math.sin(t) ** 3)
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    # Scale and center based on the specific layer's scale
    canvas_x = WIDTH / 2 + (x * scale)
    canvas_y = HEIGHT / 2 - (y * scale)
    return canvas_x, canvas_y


class TripleHeartAnimation:

    def __init__(self, root):
        self.root = root
        self.root.title("3-Line Moving Love Animation")

        # Set up canvas
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Track the starting offset parameter (t)
        self.start_t = 0.0

        # We will store tuples of (text_object, layer_scale)
        self.text_objects = []

        # Create 3 lines of text
        for scale in SCALES:
            for i in range(NUM_WORDS_PER_LINE):
                word = "Love" if i % 2 == 0 else "love"

                obj = self.canvas.create_text(
                    0,
                    0,
                    text=word,
                    fill="#FF0000",  # Bright Red
                    font=("Arial", 11, "bold"),  # Small and elegant
                    anchor="center",
                )
                # Keep track of the object and which layer scale it belongs to
                self.text_objects.append((obj, scale))

        # Start loop
        self.animate()

    def animate(self):
        # Update positions for all objects across all 3 lines
        for index, (obj, scale) in enumerate(self.text_objects):
            # Get the relative index within its own 50-word layer
            local_index = index % NUM_WORDS_PER_LINE

            # Space them evenly around the loop
            t = self.start_t + (local_index * TEXT_SPACING)
            t = t % (2 * math.pi)

            # Calculate coordinates using the layer's specific scale
            x, y = get_heart_coordinate(t, scale)
            self.canvas.coords(obj, x, y)

        # Increment movement
        self.start_t += ANIMATION_SPEED

        # Loop at ~60 FPS
        self.root.after(16, self.animate)


if __name__ == "__main__":
    window = tk.Tk()
    app = TripleHeartAnimation(window)
    window.mainloop()