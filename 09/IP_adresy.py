'''
Uvažuj, že vytváříš aplikaci, která pošle testovací zprávu (tzv. ping) počítači
s nějaou IP adresou. Napiš program, která požádá uživatele o IP adresu
a zkontroluj, zda je adresa platná. Např. adresa 325.125.100.128 není platná
(první číslo je větší než 255), adresa 152.145.146 také není platá
(jde o trojici čísel, nikoli čtveřici), adresa 192.168.1.0 je platná
(čtveřice čísel v daném rozsahu). Pro zjednodušení budeme kontrolovat pouze to,
zda je číslo v rozsahu 0 až 299.
'''

import re

reg_ex = re.compile(r'([2][0-4]\d\.|[2][5][0-5]\.|[1]?\d{1,2}\.){3}([2][0-4]\d|[2][5][0-5]|[1]?\d{1,2})')

user_input = input('Prosím zadejte IP adresu: ')

if reg_ex.fullmatch(user_input):
    print('IP adresa je platná')
else:
    print('IP adresa není platná')
    
