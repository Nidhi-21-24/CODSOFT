import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.configure(bg="#F7DC6F")  # Light yellow background

# Entry widget for displaying the input and output
entry = tk.Entry(root, width=20, font=('Arial', 28), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button click
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

# Function to handle operator buttons (+, -, *, /)
def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

# Button creation with soft colors to mimic transparency
button_1 = tk.Button(root, text="1", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=30, pady=20, font=('Arial', 18), bg="#D5E8D4", command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=30, pady=20, font=('Arial', 18), bg="#F9EBEA", command=lambda: button_operator('+'))
button_subtract = tk.Button(root, text="-", padx=30, pady=20, font=('Arial', 18), bg="#F9EBEA", command=lambda: button_operator('-'))
button_multiply = tk.Button(root, text="*", padx=30, pady=20, font=('Arial', 18), bg="#F9EBEA", command=lambda: button_operator('*'))
button_divide = tk.Button(root, text="/", padx=30, pady=20, font=('Arial', 18), bg="#F9EBEA", command=lambda: button_operator('/'))

button_equal = tk.Button(root, text="=", padx=30, pady=20, font=('Arial', 18), bg="#A9DFBF", command=button_equal)
button_clear = tk.Button(root, text="C", padx=30, pady=20, font=('Arial', 18), bg="#F7DC6F", command=button_clear)

# Place buttons in a grid
buttons = [
    button_7, button_8, button_9, button_divide,
    button_4, button_5, button_6, button_multiply,
    button_1, button_2, button_3, button_subtract,
    button_0, button_clear, button_equal, button_add
]

row_val = 1
col_val = 0
for button in buttons:
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
