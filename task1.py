#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""
import math
x = int(input("Enter Number: "))
print(x, x*2, x*3, x*4, x*5, x*6, x*7, x*8, x*9, x*10, x*11, x*12)
