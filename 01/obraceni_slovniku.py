# Napiš funkci, která ze slovníku vytvoří nový slovník, kde klíče a hodnoty budou zaměněné
# Použij dict comprehension

def obrat_slovnik(slovnik):
    return{key:item for item, key in slovnik.items()}


# Napoveda:
def napoveda(iterable1, iterable2):
    # dict comprehension:
    return {k: v for k, v in zip(iterable1, iterable2)}


iterable1 = [0, 1, 2]
iterable2 = ['a', 'b', 'c']
print(napoveda(iterable1, iterable2))
