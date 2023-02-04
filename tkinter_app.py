import tkinter as tk
import random
import tkinter.messagebox as messagebox


def main():
    # Create the main window
    root = tk.Tk()
    root.geometry("500x450")

    # Set the window title
    root.title("Password Generator")

    # Create a label to display instructions
    label = tk.Label(root, text="Choose length of the password:", font=("Arial", 20))
    label.pack()

    # Create a Scale widget to allow the user to choose the password length
    length_scale = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, resolution=1, troughcolor='blue', font=("Arial", 20), length=400)
    length_scale.pack()

    # Create checkboxes to allow the user to specify which characters to include in the password
    uppercase_var = tk.IntVar()
    uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var, font=("Arial", 20))
    uppercase_checkbox.pack()

    lowercase_var = tk.IntVar()
    lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var, font=("Arial", 20))
    lowercase_checkbox.pack()

    numbers_var = tk.IntVar()
    numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var, font=("Arial", 20))
    numbers_checkbox.pack()

    special_var = tk.IntVar()
    special_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_var, font=("Arial", 20))
    special_checkbox.pack()

    # Create a button to generate a new password
    def generate_password():
        # Check if any of the checkboxes are selected
        if not any(
                (uppercase_var.get() == 1, lowercase_var.get() == 1, numbers_var.get() == 1, special_var.get() == 1)):
            # Display an error message if no checkboxes are selected
            tk.messagebox.showerror("Error", "Please select at least one character type to include in the password.")
            return

        # Get the password length from the Scale widget
        length = int(length_scale.get())

        # Create a list of characters to include in the password
        char_list = []
        if uppercase_var.get() == 1:
            char_list += [chr(i) for i in range(65, 91)]
        if lowercase_var.get() == 1:
            char_list += [chr(i) for i in range(97, 123)]
        if numbers_var.get() == 1:
            char_list += [str(i) for i in range(0, 10)]
        if special_var.get() == 1:
            char_list += [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

        # Generate a random password
        password = ""
        for i in range(length):
            password += random.choice(char_list)

        # Update the password label
        password_label.config(text=password)

        # Create a button to copy the password to the clipboard
        def copy_to_clipboard():
            root.clipboard_clear()
            root.clipboard_append(password)

        copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 20))
        copy_button.pack()

    button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 20))
    button.pack()

    # Create a label to display the generated password
    password_label = tk.Label(root, text="", font=("Arial", 20))
    password_label.pack()

    # Run the tkinter event loop
    root.mainloop()


if __name__ == '__main__':
    main()
