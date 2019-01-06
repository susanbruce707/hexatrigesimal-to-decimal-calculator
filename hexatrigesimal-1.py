# -*- coding: utf-8 -*-
# debugging in progress, state = running, pythonicanising script.
"""
Created on Sat Jan  5 08:16:19 2019
hexatrigesimal to decimal calculator,
base 36 encoding; use of letters with digits.
And decimal to base 36.
@author: susan
"""
## create a dictionary as reference for BASE 36 calculations.
NUM = "0123456789"
WORD = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # digits of BASE 36.
BASE = {}
for i, item in enumerate(WORD): # iterate through word.
    BASE.update({WORD[i]:i}) # update BASE dictionary with key:value pair.

 

# main function, main program flow.
def main():
    """
    Display menu.
    Terminate program.
    Receive user selection.
    Calculate and display result.
    """
    menu()
    enter_select()
# display funtion, display menu.
def menu():
    """print a menu.
    """
    print(
        """
        0 Exit program.
        1 convert base 36 number to decimal.
        2 convert decimal to base 36 number.
        """
        )
# input funtion, enter menu selection.
def enter_select():
    choice = None
    select = ('0', '1', '2')
    while choice not in select:
        choice = input('Select option >')
        if choice not in select:
            print('unvalid selection made')
            choice = None
    if choice == '1':
        base36_num = enter_b36()
        convert(base36_num )
        menu()
        enter_select()
    elif choice == '2':
        dec_num = enter_dec()
        ans = dec_to_base36(dec_num)
        print("base 36 representation of decimal number", dec_num, "is", ans)
        menu()
        enter_select()
    elif choice == '0':
        print("user terminated program")
    else:
        menu()   
# input function, decimal numbers for calculation.
def enter_dec():
    dec_num  = input("please enter a Decimal number, e.g. 683248722 :> ")
    dec_num  = dec_num .upper()
    for digit in dec_num :
        if digit not in NUM:
            print(" **error** user input failed\n")
            print("do you want to re enter number")
            ans = input("y or n ")
            ans = ans.upper()
            if ans == "Y":
                dec_num  = enter_dec()
            else:
                dec_num  = "0"
    return dec_num
    
# input function, BASE 36 numbers for calculations.
def enter_b36():
    """ get user input and do error checking for ilegal digits.
    returns
    -------
    num
    """
    num = input("please enter a BASE 36 number, e.g. BASE36 :> ")
    num = num.upper()
    for digit in num:
        if digit not in WORD:
            print(" **error** user input failed\n")
            print("do you want to re enter number")
            ans = input("y or n ")
            ans = ans.upper()
            if ans == "Y":
                num = enter_b36()
            else:
                num = "0"
    return num
# function, convert base 36 number to decimal value.
def convert(base36_num):
    """ convert base 36 number to decimal value.
    prints result in decimal.
    returns
    -------
    dec
    """
    base36_num = base36_num.upper()
    base36_lst = list(base36_num)
    base36_lst.reverse()
    for i, item in enumerate(base36_lst):
        dec = (36**i) * BASE[(base36_lst[i])]
        print("Decimal value of >", base36_lst[i], "is", dec)
        base36_lst[i] = dec
    print("Sum of decimal values >", sum(base36_lst))
# convert funtion, decimal to base 36.
def dec_to_base36(dec_num):
    """
    converts decimal dec to base36 number.
    returns
    -------
    result
    """
    dec = int(dec_num )
    result = ''
    while dec > 0:
        dec1 = dec
        dec, remainder = divmod(dec, 36)
        result = WORD[remainder]+result
        print(":decimal =", dec1,
              " :mod div 36 =", dec,
              " :remainder =", remainder,
              " :base 36 =", WORD[remainder])             
    return result
main() # debugging in progress, state = running, pythonicanising script.