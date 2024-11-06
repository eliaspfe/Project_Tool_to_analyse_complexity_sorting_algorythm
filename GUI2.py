import tkinter as tk
from tkinter import ttk
from langchain_openai import ChatOpenAI
from functions import calculate_complexity, paste_example

SYSTEM_PROMPT_PATH = "sys_prompts/system_prompt1.txt"
BUBBLE_SORT_PATH = "example_algorithms/bubble_sort.txt"
INSERTION_SORT_PATH = "example_algorithms/insertion_sort.txt"
QUICK_SORT_PATH = "example_algorithms/quick_sort.txt"
MERGE_SORT_PATH = "example_algorithms/merge_sort.txt"
SELECTION_SORT_PATH = "example_algorithms/selection_sort.txt"

# Create the main application window
gui = tk.Tk()
gui.title("Big O Calc")
gui.geometry("1000x900")  # Increase window height to accommodate the button

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

button_frame = tk.Frame(master=gui, bg="#2b2d33")
button_frame.pack(fill="x", expand=True, padx=25, pady=(10, 0))

#button1
example_button = tk.Button(
    master=button_frame,
    text="Selection Sort",
    font=("Arial", 14),
    fg="#1e1f23",
    bg="#3a3d46",
    relief="flat",
    height=2,
    width=15,
    command=lambda: paste_example(code_input, SELECTION_SORT_PATH)
)
example_button.pack(side="left", padx=5, expand=True)

#button2
example_button2 = tk.Button(
    master=button_frame,
    text="Bubble Sort",
    font=("Arial", 14),
    fg="#1e1f23",
    bg="#3a3d46",
    relief="flat",
    height=2,
    width=15,
    command=lambda: paste_example(code_input, BUBBLE_SORT_PATH)
)
example_button2.pack(side="left", padx=5, expand=True)

#button3
example_button3 = tk.Button(
    master=button_frame,
    text="Insertion Sort",
    font=("Arial", 14),
    fg="#1e1f23",
    bg="#3a3d46",
    relief="flat",
    height=2,
    width=15,
    command=lambda: paste_example(code_input, INSERTION_SORT_PATH)
)
example_button3.pack(side="left", padx=5, expand=True)

#button4
example_button4 = tk.Button(
    master=button_frame,
    text="Quick Sort",
    font=("Arial", 14),
    fg="#1e1f23",
    bg="#3a3d46",
    relief="flat",
    height=2,
    width=15,
    command=lambda: paste_example(code_input, QUICK_SORT_PATH)
)
example_button4.pack(side="left", padx=5, expand=True)

#button5
example_button5 = tk.Button(
    master=button_frame,
    text="Merge Sort",
    font=("Arial", 14),
    fg="#1e1f23",
    bg="#3a3d46",
    relief="flat",
    height=2,
    width=15,
    command=lambda: paste_example(code_input, MERGE_SORT_PATH)
)
example_button5.pack(side="left", padx=5, expand=True)


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
    bg="#3a3d46",
    relief="flat",
    height=2,
    command=lambda: calculate_complexity(code_input.get("1.0", "end-1c"), output_label)  # Call the function
)

calculate_button.pack(fill="both", padx=80, pady=(0, 20))  # Padding below the button

output_frame = tk.Frame(master=gui, bg="#2b2d33")
output_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

# LLM Output label
output_label = tk.Text(
    master=output_frame,
    font=("Arial", 16),
    fg="lightgrey",
    bg="#2b2d33",
    borderwidth=0,
    insertbackground="#2b2d33",
    highlightthickness=0
)
output_label.insert(tk.END, "Enter your code here...")
output_label.config(state="disabled")
output_label.pack(fill="both", expand=True, padx=10, pady=10)  # Padding below the subtitle

# Run the main event loop
gui.mainloop()
