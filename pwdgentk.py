# Import tkinter, our graphics library
from tkinter import *
from tkinter import ttk

# Import Python's Random module
import random

# Constants
chars = list("abcdefghijklmonpqrstuvqyz")
chars_upper = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
nums = list(range(0, 10))
syms = list("!\"Â£$%^&*()_+-=[]{};':@',./<>?")

# Variables
options = [chars, chars_upper, nums, syms]
max_len = 15

# Defining our input and output boxes
pwdlen_input = None
pwdlen_output = None

# Create the core of our window
root = Tk()
root.title("pwdgen")
# Functions
def generate(max_len):
    out = ""

    while len(out) <= max_len:
        type_of_char = random.choice(options)
        out += str(random.choice(type_of_char))

    return out

# This function is called when the button is clicked.
def clicked_button():
    # Clear our computers clipboard
    root.clipboard_clear()

    # Get the text from our input box
    l = pwdlen_input.get()

    # Checking if input is a valid number.
    if not l.isdigit():
        pwdlen_output.delete(0, END)
        pwdlen_output.insert(0, "Length is not a valid number.")
        return

    pwd = generate(int(l))

    root.clipboard_append(pwd)
    pwdlen_output.delete(0, END)
    pwdlen_output.insert(0, pwd)

def modifier(m):
    l = pwdlen_input.get()
    new_len = 0
    if not l.isdigit():
        pwdlen_output.delete(0, END)
        pwdlen_output.insert(0, "Length is not a valid number.")
        return

    if m == "+":
           new_len = int(l) + 1
    if m == "-":
           new_len = int(l) - 1

    pwdlen_input.delete(0, END)
    pwdlen_input.insert(0, str(new_len))

#root.set_title()
# Add a frame to the window, a container that we can store elements in
frm = ttk.Frame(root, padding=10)
# Place it on the grid
frm.grid()

ttk.Label(frm, text="Length: ").grid(row=0, column=0)
# Create a text input field
pwdlen_input = ttk.Entry(frm, width=30)
pwdlen_input.insert(0, "20")
pwdlen_input.grid(column=1,row=0)

# Create a button
gen = ttk.Button(frm, text="Generate", command=lambda: clicked_button())
gen.grid(column=2, row=0)
ttk.Button(frm, text="-", command=lambda: modifier("-")).grid(column=3, row=0)
ttk.Button(frm, text="+", command=lambda: modifier("+")).grid(column=4, row=0)

pwdlen_output = ttk.Entry(frm, width=70)
pwdlen_output.grid(column=0,row=1, columnspan=5)

root.mainloop()