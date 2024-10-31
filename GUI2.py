import tkinter as tk
from tkinter import ttk
from langchain_openai import ChatOpenAI
from functions import calculate_complexity


# Create the main application window
gui = tk.Tk()
gui.title("Big O Calc")
gui.geometry("600x600")  # Increase window height to accommodate the button

# Set a dark theme
gui.configure(bg="#2b2d33")  # Background color similar to the image

# Create the title label
title_label = tk.Label(
    master=gui,
    text="Big O Calc",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#2b2d33"
)
title_label.pack(pady=(20, 5))  # Add some padding at the top

# Create the subtitle label
subtitle_label = tk.Label(
    master=gui,
    text="Calculate the time and space complexity of your code using Big O notation",
    font=("Arial", 16),
    fg="lightgrey",
    bg="#2b2d33"
)
subtitle_label.pack(pady=(0, 10))  # Padding below the subtitle

# Create a frame for the input area
input_frame = tk.Frame(master=gui, bg="#2b2d33")
input_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

# Create a text widget for code input
code_input = tk.Text(
    master=input_frame,
    wrap="word",
    font=("Courier New", 12),
    bg="#1e1f23",
    fg="white",
    insertbackground="white",  # Cursor color
    borderwidth=0,
    relief="flat"
)
code_input.pack(fill="both", expand=True, padx=10, pady=10)

# Create the Calculate button
calculate_button = tk.Button(
    gui,
    text="Calculate",
    font=("Arial", 16, "bold"),
    fg="#1e1f23",
    activebackground="green",
    activeforeground="#1e1f23",
    relief="flat",
    command=lambda: calculate_complexity(code_input.get("1.0", "end-1c"), output_label)  # Call the function
)

calculate_button.pack(fill="both", expand=True, padx=80, pady=(0, 20))  # Padding below the button

# LLM Output label
output_label = tk.Label(
    master=gui,
    text="This is where the output will go",
    font=("Arial", 16),
    fg="lightgrey",
    bg="#2b2d33"
)
output_label.pack(padx= 80, pady=(0, 10))  # Padding below the subtitle

# Run the main event loop
gui.mainloop()
