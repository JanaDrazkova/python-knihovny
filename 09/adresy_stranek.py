'''
 Napiš program, který z proměnné email_s_radami vytáhne všechny webové stránky,
 které jsou tam zmíněny.
'''

email_s_radami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu
článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci.
http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky,
rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je
placený web, který ale kvalitou kurzů víceméně nemá konkurenci.
Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
"""

# Jde mi o to, jak vyhledat reg.ex., který má několik group. Jestli tomu správně rozumím, nejde to findall, ale musím na to přes match

import re

rv = re.compile(r"https?://([a-zA-Z\d]\.|([a-zA-Z\d][a-zA-Z\d\-]*[a-zA-Z\d])+\.)+[a-zA-Z\d]+") #domena nesmi zacinat ani končit pomlckou
work_email = email_s_radami
while rv.search(work_email):
    match = rv.search(work_email)
    print(match.group())
    work_email = work_email[match.end():]