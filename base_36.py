# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:41:08 2018
hexatrigesimal to decimal calculator,
base 36 encoding; use of letters with digits.
@author: susan
"""
## create a dictionary as reference for BASE 36 calculations
WORD = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # digits of BASE 36
BASE = {}
for i, item in enumerate(WORD): # iterate through word
    BASE.update({WORD[i]:i}) # update BASE dictionary with key:value pair
# input function, BASE 36 numbers for calculations.
def enter_num():
    """ get user input and do error checking for illegal digits.
    returns
    -------
    num
    """
    num = input("please enter a BASE 36 number, e.g. A36Z :> ")
    num = num.upper()
    for digit in num:
        digit = digit.upper()
        if digit not in WORD:
            print(" **error** user input failed\n")
            print("do you want to re enter number")
            ans = input("y or n ")
            ans = ans.upper()
            if ans == "Y":
                num = enter_num()
            else:
                num = None
    return num
# make list function.
def mk_num_lst(num):
    """ make BASE 36 number from user into a list.
    reverse list so digit are read left to right.
    returns
    -------
    num_lst
    """
    num_lst = []
    for digit in num:
        num_lst.append(digit)
    num_lst.reverse()
    return num_lst
# convert function.
def convert(num_lst):
    """ convert each digit to power of 36 appropriately.
    prints result in decimal.
    returns
    -------
    dec
    """
    dec = 0
    for i in range(0, len(num_lst)):
        print("position right to left is >", i+1,
              "value is ", BASE[(num_lst[i])],
              "decimal value is",
              (36**i) * BASE[(num_lst[i])])
        dec += (36**i) * BASE[(num_lst[i])]
    return dec
# main program flow function.
def main():
    """
    process valid user input or
    terminate program on failed input.
    """
    num = enter_num()
    if num is not None:
        num_lst = mk_num_lst(num)
        dec = convert(num_lst)
        print("decimal value of BASE 36 number", num, "is", dec)
    else:
        print("user terminated program")
# program start.
main()
