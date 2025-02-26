#----- HAD A VELBLOUD
import sys

variable = sys.argv[1]

def exchange_2letters(string, position, letter):
    '''Replace 2 letters of string after given position with given letter'''
    return string[:position] + letter + string[position+2:]

# replace _a with A
while "_" in variable:
    position = variable.index("_")
    variable = exchange_2letters(variable, position, variable[position+1].upper())


print(variable)