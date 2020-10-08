#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""


def isInteger(a):
    if a % 1 == 0:
        result = True
        return result
    else:
        result = False
        return result
