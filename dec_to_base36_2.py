# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 23:38:34 2018
Decimal to hexatrigesimal calculator.
convert decimal number to base 36 encoding; use of letters with digits. 
@author: susan
"""

def dec_to_base36(dec):
    """
    converts decimal dec to base36 number.
    returns
    -------
    sign+result
    """
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    sign = '-' if dec < 0 else ''
    dec = abs(dec)
    result = ''

    while dec > 0:
        dec, remainder = divmod(dec, 36)
        result = chars[remainder]+result

    return sign+result
dec = int(input("please enter a Decimal number, e.g. 683248722 :> "))
A = dec_to_base36(dec)
print(A)
