import re

kod = """
sender_field_title = "Příjemce"
copy_field_title = "Kopie"
if blind_copy == True:
    blind_copy_title = "Skrytá kopie"
if action == "send":
    button_title = "Odeslat"
else:
    button_title = "Uložit koncept"
"""

reg_ex_equality = re.compile(r'\w+ = \"[\w ]+\"')
assigments = reg_ex_equality.findall(kod)

reg_ex_string = re.compile(r'\"[\w ]+\"')
for assigment in assigments:
    print(reg_ex_string.findall(assigment)[0])
    