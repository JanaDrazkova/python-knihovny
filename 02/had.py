#----- HAD A VELBLOUD
import sys

input_text = sys.argv[1]

def replace_2letters_with_one(string, position, letter):
    '''Replace 2 letters of string after given position with given letter'''
    return string[:position] + letter + string[position+2:]

# replace _a with A
while "_" in input_text:
    position = input_text.index("_")
    input_text = replace_2letters_with_one(input_text, position, input_text[position+1].upper())
    if len(input_text) > position+1:
        input_text = replace_2letters_with_one(input_text, position, input_text[position+1].upper())
    else:
        input_text = input_text[:-1]


print(input_text)