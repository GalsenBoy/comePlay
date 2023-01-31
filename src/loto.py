import random
loto = list(range(1, 50))

to_choose = []

for j in loto:
    to_choose.append(random.choice(loto))
    if len(to_choose) == 6:
        break

#print(to_choose)
choice = int(input("Essayer de diviner un nombre dans les 6 boules de tirage entre 1 et 49 \n"))

if choice in to_choose:
    print(f"Bravo!!! {choice} fait parti dans la liste a trouvé")
else:
    print("Dommage vous avez perdu votre argent lol ")
