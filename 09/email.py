'''
Uprav program na ověření e-mailu tak, aby akceptoval i e-maily,
které mají v první části tečku, např. jiri.pesik@python.cz.
'''
import re

regularni_vyraz = re.compile(r"(\w+\.?)+\w+@\w+\.cz")  # pred zavinacem tecku nepripousti
email = input("Zadej e-mail: ")
hledani = regularni_vyraz.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")