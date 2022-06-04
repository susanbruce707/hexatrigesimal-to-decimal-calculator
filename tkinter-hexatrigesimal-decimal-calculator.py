#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:37:58 2021
tkinter based hexatrigesimal <=> decimal calculator.
@author: susan
"""
################################################################
# TODO list.
# limit number of characters allowed as input to entry boxes Respectively.
# 30 z's equals a 47 digit Dec number 48873677980689257489322752273774603865660850175
# add help menu giving info on usage
# add copy and paste functionality.
#################################################################
# WORD1 is digits of BASE 36 used for decimal to base 36 conversion, Z representing a value of 35.
# WORD2 is digits of BASE 37 used for decimal to base 37 conversion, space representing a value of 36.
NUM = "0123456789"
WORD1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORD2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
BASE1 = {}
BASE2 = {}
for i, item in enumerate(WORD1): # iterate through word.
    BASE1.update({WORD1[i]:i}) # update BASE dictionary with key:value pair.
for i, item in enumerate(WORD2): # iterate through word.
    BASE2.update({WORD2[i]:i}) # update BASE dictionary with key:value pair.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmb
# Create the root window
root = tk.Tk()
# configure root
root.title('tkinter based (hexatrigesimal <=> decimal) calculator')
root.geometry('950x170+300+300')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.configure(bg='#FFAA00')
# variables
dec_var = tk.StringVar(root)
hexa_var = tk.StringVar(root)
check_bool_var = tk.BooleanVar(root)
# message for messagebox
title = "INVALID ENTRY"
message1 = ("Only one entry box can contain a number before calculation is made")
message2 = ("Maximum number of characters for base 36 or base 37 is 30")
message3 = ("Maximum number of characters for base 36 or base 37 is 46")
detail1 = ("   Clear ?")
detail2 = (" Continue ?")
# functions
def validate_dec(input, i):
    """validates input is only integer decimal"""
    if i == '46':
        tkmb.showinfo(title=title, message=message3, detail = detail2)
    if input in NUM:
        return True
    elif input == "":
        return True
    else:
        return False
def validate_hexa(input, i):
    """validates input is only alphanumeric"""
    if i == '29':
        tkmb.showinfo(title=title, message=message2, detail = detail2)
        return False
    if check_bool_var.get() == 1:
        word = WORD2
    else:
        word = WORD1
    if input.upper() in word:
        return True
    elif input == "":
        return True
    else:
        return False
def error_mes(m):
    """shows warning message"""
    tkmb.showwarning(title=title, message=m, detail = detail1)
    clear()
def clear():
    """clears entry boxes"""
    dec_var.set("")
    hexa_var.set("")
    check_bool_var.set(False)
def calc_val():
    """checks which entry boxes are used and branches accordingly to calculation"""
    if dec_var.get() > "" and hexa_var.get() > "":
        error_mes(message1)
    if dec_var.get() > "":
        dec_to_hexa()
    elif hexa_var.get() > "":
        hexa_to_dec()
# function, convert base 36 number to decimal value.
def hexa_to_dec():
    """converts base 36 or base 37 number to decimal value."""
    if check_bool_var.get() == 1:
        base = 37
        dic_base = BASE2
    else:
        base = 36
        dic_base = BASE1
    hexa = hexa_var.get()
    hexa = hexa.upper()
    hexa_lst = list(hexa)
    hexa_lst.reverse()# for item in reversed(list_whatever):
    for i, item in enumerate(hexa_lst):
        dec = (base**i) * dic_base[(hexa_lst[i])]
        hexa_lst[i] = dec
    dec_var.set(str(sum(hexa_lst)))
    print("hexa["+str(hexa)+"] in base"+str(base), " to decimal", "result["+str(sum(hexa_lst))+"]\n")
# function to convert decimal to base 36 number
def dec_to_hexa():
    """converts decimal value to base 36 or base 37 number."""
    if check_bool_var.get() == 1:
        base = 37
        word = WORD2
    else:
        base = 36
        word = WORD1
    dec = dec_var.get()
    dec = int(dec)
    d = dec
    result = ''
    while dec > 0:
        dec, remainder = divmod(dec, base)
        result = word[remainder]+result
    hexa_var.set(str(result))
    print("decimal["+str(d)+"] to hexa base"+str(base), "result["+str(result)+"]\n")
# labels
instruc_lable = tk.Label(root, text="Enter the number to convert in one of the entry boxes")
dec_label = tk.Label(root, text="Decimal")
sep_label = tk.Label(root, text="********")
hexa_label = tk.Label(root, text="Hexatrigesimal")
sep1 = ttk.Separator(root, orient=tk.HORIZONTAL)
instruc_lable.grid(columnspan=3, row=0, sticky="we", padx=5, pady=5)
dec_label.grid(column=0, row=1, sticky="we", padx=5, pady=10)
sep_label.grid(column=1, row=1, sticky="we", padx=70, pady=10)
hexa_label.grid(column=2, row=1, sticky="we", padx=5, pady=10)
sep1.grid(row=3)
# entry's
dec_entry = tk.Entry(root, textvariable=dec_var, width=50, bd=7)
hexa_entry = tk.Entry(root, textvariable=hexa_var, width=32, bd=7)
dec_entry.grid(column=0, row=2)
hexa_entry.grid(column=2, row=2)
# entry Binds
dec_entry.bind('<Return>',lambda event:calc_val())
hexa_entry.bind('<Return>',lambda event:calc_val())
# validation register
validate_dec_reg = root.register(validate_dec)
dec_entry.config(validate ="key",
        validatecommand =(validate_dec_reg, '%S', '%i'))
validate_hexa_reg = root.register(validate_hexa)
hexa_entry.config(validate ="key",
        validatecommand =(validate_hexa_reg, '%S', '%i'))
# buttons
clear_button = tk.Button(root, text=" * CLEAR * ", command=clear)
calc_button = tk.Button(root, text=" CALCULATE ", command=calc_val)
clear_button.grid(column=1, row=2, pady=10)
calc_button.grid(column=1, row=4, pady=15)
# checkbutton
base37_check = ttk.Checkbutton(root, variable=check_bool_var, text="Base 37 special", onvalue=1, offvalue=0)
base37_check.grid(column=2, row=4)
###############
# Execute App #
###############
root.mainloop()
