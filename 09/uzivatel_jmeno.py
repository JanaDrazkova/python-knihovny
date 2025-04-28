'''
Náš systém vyžaduje od uživatele zadání uživatelského jména.
Uživatelské jméno smí obsahovat pouze malá písmena a
smí být maximálně 8 znaků dlouhé. Požádej uživatele o zadání
uživatelského jména a pomocí regulárního výrazu vyhodnoť, zda je zadané správné.
'''

import re

rv = re.compile(r"[a-z]{1,8}") 		#maximalne 8 malych pismen
user_input = input('Zadejte prosím vaše uživatelské jméno: ')

if rv.fullmatch(user_input):
    print("Uživatelské heslo je správné.")
else:
    print("Uživatelské heslo není správné.")




