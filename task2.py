#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(numlist):
    a = numlist[0]
    for i in numlist:
        if i > a:
            a = i
    return a
numberlist = [5,1,12.3]
b = largest(numberlist)
print(b)
