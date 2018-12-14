# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:34:24 2018
hexatrigesimal to decimal calculator,
base 36 encoding; use of letters with digits.
@author: susan
"""
## create a dictionary as reference for base 36 calculations
word ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # digits of base 36
temp ={}
base ={}
for item in range(len(word)): # iterate through word 
    a=word[item] # create key
    b=item # create key value
    temp={a:b} # create temp dictionary of key value pair
    base.update(temp) # update base dictionary
# input base 36 numbers for calculations        
def enter_num():
    """ get user input and send for error checking to error_chk().
    returns
    -------
    num
    """
    num = error_check()
    if "ilegal" in num:
        print(" **error** user input failed\n")
        print("do you want to re enter number")
        ans= input("y or n ")
        ans=ans.upper()
        if ans=="Y":
            num = error_check()
            return num        
    else:
        return num
# error check user input for ilegal digits
def error_check():
    """# convert num to upper case and check for digits not in word.
    if user entry ilegal; user offered second try.
    returns
    -------
    chk  
    """
    num = input("please enter a base 36 number, e.g. A36Z :> ")
    chk=""
    for digit in num:
        digit=digit.upper()        
        if digit in word:
            chk += digit
        else:            
            chk += "*"
    if "*" in chk:
        return "ilegal"
    else:
        return chk

def mk_lst(num):
    """ make base 36 number from user into a list.
    returns
    -------
    lst
    """
    lst=[]
    for digit in num:
        lst.append(digit)
    return lst

def convert(x):
    """ convert each digit to power of 36 appropriately.
    prints result in decimal.
    returns
    -------
    dec
    """
    dec=0
    for i in range(0,len(x)):
        print("position right to left is-", i+1,
              "value is ", base[(x[i])],
              "decimal value is",
              (36**i)* base[(x[i])])
        dec+=(36**i)* base[(x[i])]   
    return dec
#
def main():    
    num = enter_num()
    if num != None:
        x = mk_lst(num)
        x.reverse() # reverse list so digit are read left to right.
        dec=convert(x)
        print("decimal value of base 36 number", num, "is", dec)
    else:
        print("user terminated program")
main()


