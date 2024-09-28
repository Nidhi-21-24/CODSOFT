import tkinter as tk
import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the remaining length of the password with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def generate():
    try:
        length = int(length_entry.get())
        if length < 8:
            result_label.config(text="Password length must be at least 8 characters.", fg="white")
            return
        generated_password = generate_password(length)
        result_label.config(text=f"Generated Password: {generated_password}", fg="white")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.", fg="white")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="black")  # Black background

# Create and place the widgets
length_label = tk.Label(root, text="Enter Password Length (min 8):", bg="black", fg="white", font=('Arial', 14))
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=10, font=('Arial', 14))
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate, bg="#76D7C4", fg="white", font=('Arial', 14))  # Light green
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="black", fg="white", font=('Arial', 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
