import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.geometry("200x100")

# Set up style for ttk.Button
style = ttk.Style()
style.configure("TButton", font=("Arial", 16, "bold"), background="blue", foreground="white")
style.map("TButton",
          background=[("active", "green")],
          foreground=[("active", "yellow")])

# Create the button using the style
calculate_button = ttk.Button(
    gui,
    text="Calculate",
    style="TButton",
    command=lambda: print("Calculate button clicked")
)
calculate_button.pack(pady=20)

gui.mainloop()
