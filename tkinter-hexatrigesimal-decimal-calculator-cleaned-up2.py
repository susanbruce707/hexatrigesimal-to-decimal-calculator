#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:37:58 2021
tkinter based hexatrigesimal <=> decimal calculator.
@author: susan
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmb

# Constants
NUM = "0123456789"
WORD1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORD2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
BASE1 = {char: index for index, char in enumerate(WORD1)}
BASE2 = {char: index for index, char in enumerate(WORD2)}
TITLE = "INVALID ENTRY"
MESSAGE1 = "Only one entry box can contain a number before calculation is made"
MESSAGE2 = "Maximum number of characters for base 36 or base 37 is 30"
MESSAGE3 = "Maximum number of characters for base 36 or base 37 is 46"
DETAIL1 = "   Clear ?"
DETAIL2 = " Continue ?"
HELP_MESSAGE = "This is a tkinter based hexatrigesimal to decimal calculator.\n\n1. Enter the number to convert in one of the entry boxes.\n2. Press 'Enter' to calculate.\n3. Use the right-click menu to copy and paste values.\n4. Use the 'Base 37 special' checkbox to switch between base 36 and base 37.\n\nEnjoy!"

# Popup menu functions
def show_popup_menu(event):
    global clicked_widget
    clicked_widget = event.widget
    popup_menu.post(event.x_root, event.y_root)

def copy():
    root.clipboard_clear()
    root.clipboard_append(clicked_widget.get())

def paste():
    clicked_widget.insert(tk.END, root.clipboard_get())

def copy_results():
    root.clipboard_clear()
    output = "\n".join(map(str, results))
    root.clipboard_append(output)

def show_help():
    tkmb.showinfo("Help", HELP_MESSAGE)

def exit_program():
    root.destroy()

# Validation functions
def validate_dec(input_val, index):
    """Validates input as integer decimal"""
    if index == '46':
        tkmb.showinfo(title=TITLE, message=MESSAGE3, detail=DETAIL2)
    return input_val in NUM or input_val == ""

def validate_hexa(input_val, index):
    """Validates input as alphanumeric"""
    if index == '29':
        tkmb.showinfo(title=TITLE, message=MESSAGE2, detail=DETAIL2)
        return False
    word = WORD2 if check_bool_var.get() else WORD1
    return input_val.upper() in word or input_val == ""

# Error message function
def error_mes(message):
    """Shows warning message"""
    tkmb.showwarning(title=TITLE, message=message, detail=DETAIL1)
    clear()

# Clear entries function
def clear():
    """Clears entry boxes"""
    dec_var.set("")
    hexa_var.set("")
    check_bool_var.set(False)

# Calculate values function
def calc_val():
    """Checks which entry box is used and branches accordingly to calculation"""
    if dec_var.get() and hexa_var.get():
        error_mes(MESSAGE1)
    elif dec_var.get():
        dec_to_hexa()
    elif hexa_var.get():
        hexa_to_dec()

# Convert base 36 number to decimal value function
def hexa_to_dec():
    """Converts base 36 or base 37 number to decimal value"""
    base = 37 if check_bool_var.get() else 36
    dic_base = BASE2 if check_bool_var.get() else BASE1
    hexa = hexa_var.get().upper()
    dec_val = sum((base ** i) * dic_base[char] for i, char in enumerate(reversed(hexa)))
    dec_var.set(str(dec_val))
    results.append(f"hexa[{hexa}] in base{base} to decimal result[{dec_val}]")
    print(f"hexa[{hexa}] in base{base} to decimal result[{dec_val}]")

# Convert decimal to base 36 number function
def dec_to_hexa():
    """Converts decimal value to base 36 or base 37 number"""
    base = 37 if check_bool_var.get() else 36
    word = WORD2 if check_bool_var.get() else WORD1
    dec = int(dec_var.get())
    result = ''
    while dec:
        dec, remainder = divmod(dec, base)
        result = word[remainder] + result
    hexa_var.set(result)
    results.append(f"decimal[{dec}] to hexa base{base} result[{result}]")
    print(f"decimal[{dec}] to hexa base{base} result[{result}]")

# Main Application
root = tk.Tk()
root.title('tkinter based (hexatrigesimal <=> decimal) calculator')
root.geometry('950x170+300+300')
root.configure(bg='#FFAA00')

# Configure root grid
for col in range(3):
    root.columnconfigure(col, weight=1)
for row in range(5):
    root.rowconfigure(row, weight=1)

# Variables
dec_var = tk.StringVar(root)
hexa_var = tk.StringVar(root)
check_bool_var = tk.BooleanVar(root)
results = []

# Popup menu
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Copy", command=copy)
popup_menu.add_command(label="Paste", command=paste)

# Labels
instruc_label = tk.Label(root, text="Enter the number to convert in one of the entry boxes")
dec_label = tk.Label(root, text="Decimal")
sep_label = tk.Label(root, text="********")
hexa_label = tk.Label(root, text="Hexatrigesimal")
sep1 = ttk.Separator(root, orient=tk.HORIZONTAL)

instruc_label.grid(columnspan=3, row=0, sticky="we", padx=5, pady=5)
dec_label.grid(column=0, row=1, sticky="we", padx=5, pady=10)
sep_label.grid(column=1, row=1, sticky="we", padx=70, pady=10)
hexa_label.grid(column=2, row=1, sticky="we", padx=5, pady=10)
sep1.grid(row=3)

# Entries
dec_entry = tk.Entry(root, textvariable=dec_var, width=50, bd=7)
hexa_entry = tk.Entry(root, textvariable=hexa_var, width=32, bd=7)
dec_entry.grid(column=0, row=2)
hexa_entry.grid(column=2, row=2)

# Entry binds
dec_entry.bind('<Return>', lambda event: calc_val())  # Press-Return event
hexa_entry.bind('<Return>', lambda event: calc_val())  # Press-Return event
dec_entry.bind("<Button-3>", show_popup_menu)  # Right-click event
hexa_entry.bind("<Button-3>", show_popup_menu)  # Right-click event

# Validation register
validate_dec_reg = root.register(validate_dec)
dec_entry.config(validate="key", validatecommand=(validate_dec_reg, '%S', '%i'))
validate_hexa_reg = root.register(validate_hexa)
hexa_entry.config(validate="key", validatecommand=(validate_hexa_reg, '%S', '%i'))

# Buttons
clear_button = tk.Button(root, text=" * CLEAR * ", command=clear)
calc_button = tk.Button(root, text=" CALCULATE ", command=calc_val)
clear_button.grid(column=1, row=2, pady=10)
calc_button.grid(column=1, row=4, pady=15)

# Checkbutton
base37_check = ttk.Checkbutton(root, variable=check_bool_var, text="Base 37 special", onvalue=1, offvalue=0)
base37_check.grid(column=2, row=4)

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit program", command=exit_program)
file_menu.add_command(label="Copy results", command=copy_results)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=show_help)

# Execute App
root.mainloop()
