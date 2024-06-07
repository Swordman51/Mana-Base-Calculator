import numpy
import re
from functions import *

file = open("example.txt")
print('\n')
print("Welcome to the Magic Manabase Calculator" + '\n')
print('\n' + "Please enter your list here using \"Copy for Moxfield\"" +"\n")

test = list(multiline_input())

formatted = [mysplit(s) for s in test]
   

print(formatted)
        




## For MDFC Lands only put front face