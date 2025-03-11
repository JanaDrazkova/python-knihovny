# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
   return [f'{minuty // 60}:{minuty % 60:02}' for minuty in vstup]

 
