"""
write a program that will as te user for a number (integer only)
and return a statement that the number is even or odd.
"""


x = float(input('Please enter a number: '))

if (x%2 == 0):
    print (" your answer is Even")

elif (x%2 == 1):
    print (" your answer is odd")