liste = [2,3,4]

def produkt(liste):
    if len(liste) == 0:
        return 0

    for zahl in liste:
        produkt = 1
        produkt = produkt * zahl
    return produkt

print(produkt(liste))