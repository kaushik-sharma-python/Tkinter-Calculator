from tkinter import *

# Create main window
root = Tk()
root.title("Tkinter Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Display
entry = Entry(root, width=18, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variables
first_number = 0
operation = ""

# Insert numbers
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Clear display
def button_clear():
    entry.delete(0, END)

# Addition
def button_add():
    global first_number
    global operation
    first_number = int(entry.get())
    operation = "+"
    entry.delete(0, END)

# Subtraction
def button_subtract():
    global first_number
    global operation
    first_number = int(entry.get())
    operation = "-"
    entry.delete(0, END)

# Multiplication
def button_multiply():
    global first_number
    global operation
    first_number = int(entry.get())
    operation = "*"
    entry.delete(0, END)

# Division
def button_divide():
    global first_number
    global operation
    first_number = int(entry.get())
    operation = "/"
    entry.delete(0, END)

# Calculate result
def button_equal():
    second_number = int(entry.get())
    entry.delete(0, END)

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            entry.insert(0, "Error")
            return
        result = first_number / second_number
    else:
        result = ""

    entry.insert(0, result)

# Buttons
Button(root, text="7", width=8, height=3, command=lambda: button_click(7)).grid(row=1, column=0)
Button(root, text="8", width=8, height=3, command=lambda: button_click(8)).grid(row=1, column=1)
Button(root, text="9", width=8, height=3, command=lambda: button_click(9)).grid(row=1, column=2)
Button(root, text="/", width=8, height=3, command=button_divide).grid(row=1, column=3)

Button(root, text="4", width=8, height=3, command=lambda: button_click(4)).grid(row=2, column=0)
Button(root, text="5", width=8, height=3, command=lambda: button_click(5)).grid(row=2, column=1)
Button(root, text="6", width=8, height=3, command=lambda: button_click(6)).grid(row=2, column=2)
Button(root, text="*", width=8, height=3, command=button_multiply).grid(row=2, column=3)

Button(root, text="1", width=8, height=3, command=lambda: button_click(1)).grid(row=3, column=0)
Button(root, text="2", width=8, height=3, command=lambda: button_click(2)).grid(row=3, column=1)
Button(root, text="3", width=8, height=3, command=lambda: button_click(3)).grid(row=3, column=2)
Button(root, text="-", width=8, height=3, command=button_subtract).grid(row=3, column=3)

Button(root, text="0", width=8, height=3, command=lambda: button_click(0)).grid(row=4, column=0)
Button(root, text="C", width=8, height=3, command=button_clear).grid(row=4, column=1)
Button(root, text="=", width=8, height=3, command=button_equal).grid(row=4, column=2)
Button(root, text="+", width=8, height=3, command=button_add).grid(row=4, column=3)

root.mainloop()