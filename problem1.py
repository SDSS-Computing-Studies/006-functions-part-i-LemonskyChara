#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math
def hypotenuse(a):
    if a[2] == True:
        b = a[0]
        if a[0] > a[1]:
            d = math.sqrt(a[0] ** 2 - a[1] ** 2)
            return d
        elif a[1] > a[0]:
            d = math.sqrt(a[1] ** 2 - a[2] ** 2)
            return d
    elif a[2] == False:
        c = math.sqrt(a[0] ** 2 + a[1] ** 2)
        return c
