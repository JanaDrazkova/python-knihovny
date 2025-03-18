hlasy = [
    [78774, 43179, 225111, 144799, 242854],
    [91062, 22451, 17475, 53391, 46450],
    [179186, 216499, 4493, 156305, 61222],
    [9619, 53476, 926, 64737, 34566],
    [66904, 85730, 27271, 12964, 38041],
    [118755, 1929, 30426, 25178, 31952],
    [64467, 40993, 81181, 39392, 4335],
    [11221, 97970, 26179, 98539, 112578],
    [171064, 7638, 8752, 96666, 39738],
    [74235, 101680, 18920, 45904, 1922],
    [39309, 1505, 10531, 30458, 40228],
    [131584, 1812, 241122, 22267, 99326],
    [194133, 39985, 200997, 28229, 20780],
    [66188, 51607, 15977, 177272, 17664]
]

kandidati = {0: "Igor Rezek", 1: "Augustýn Doležal", 2:"Vladan Bednář", 3:"Ondřej Brotz", 4:"Radim Kašpar"}
kraje = {0: "Hlavní město Praha",
         1: "Jihočeský kraj",
         2: "Jihomoravský kraj",
         3: "Karlovarský kraj",
         4: "Kraj Vysočina",
         5: "Královéhradecký kraj",
         6: "Liberecký kraj",
         7: "Moravskoslezský kraj",
         8: "Olomoucký kraj",
         9: "Pardubický kraj",
         10: "Plzeňský kraj",
         11: "Středočeský kraj",
         12: "Ústecký kraj",
         13: "Zlínský kraj"}

#Otazka 1
soucet_kandidatu = [sum([kraj[i] for kraj in hlasy]) for i in range(len(kandidati))]
for i in range(5):
    print(kandidati[i], ":", soucet_kandidatu[i])
    
# Otazka 2
vitez = soucet_kandidatu.index(max(soucet_kandidatu))
print(f'První kolo vyhrál {kandidati[vitez]}.')

# Otazka 3
volebni_ucast = [sum(kraj) for kraj in hlasy]
max_ucast = volebni_ucast.index(max(volebni_ucast))
min_ucast = volebni_ucast.index(min(volebni_ucast))

print(f"Nejvyšší volební účast byla v/ve {kraje[max_ucast]}.")
print(f"Nejvyšší volební účast byla v/ve {kraje[min_ucast]}.")

# Otazka 4
vitez_v_kraji = [kandidati[kraj.index(max(kraj))] for kraj in hlasy]

# Otazka 5
procentualni_zisk = [[round(kraj[i]/sum(kraj)*100,1) for i in range(len(kandidati))] for kraj in hlasy]