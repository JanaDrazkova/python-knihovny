'''
Napiš program, který vypíše všechna telefonní čísla,
která jsou v textovém souboru zmíněna.

Nahraď tato telefonní čísla nějakým řetězcem (např. "XXX"),
aby nebyla v záznamech dostupná.
'''

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

import re

rv = re.compile(r"\+420\d{9}")

phone_nums = rv.findall(zaznamy)
[print(num) for num in phone_nums]
  
zaznamy_without_phone_num = rv.sub("X" * 13, zaznamy)
