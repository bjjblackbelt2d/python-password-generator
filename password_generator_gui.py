import tkinter as tk
import string
import random
from csv import writer

def generate_password():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    platform = platform_var.get()
    pass_length = int(length_var.get())
    s = []
    s.extend(list(lower_case))
    s.extend(list(upper_case))
    s.extend(list(digits))
    s.extend(list(symbols))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    password_var.set(password)
    passdata = [platform, password]
    with open('pass.csv', 'a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label and entry for the platform name
platform_label = tk.Label(window, text="Platform:")
platform_label.pack()
platform_var = tk.StringVar()
platform_entry = tk.Entry(window, textvariable=platform_var)
platform_entry.pack()

# Create a label and entry for the password length
length_label = tk.Label(window, text="Password length:")
length_label.pack()
length_var = tk.StringVar()
length_entry = tk.Entry(window, textvariable=length_var)
length_entry.pack()

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(window, text="Generated Password:")
password_label.pack()
password_var = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password_var, state="readonly")
password_entry.pack()

# Start the main event loop
window.mainloop()