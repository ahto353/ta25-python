# Lemmikpuuviljade list
puuviljad = ["banaan", "õun", "maasikas"]

# Väljasta kogu list
print("Algne list:", puuviljad)

# Väljasta listi esimene väärtus
print("Esimene puuvili:", puuviljad[0])

# Lisa listi lõppu uus puuvili
puuviljad.append("pirn")
print("Pärast uue puuvilja lisamist:", puuviljad)

# Väljasta listi viimane väärtus
print("Viimane puuvili:", puuviljad[-1])

# Muuda ühe elemendi väärtust
puuviljad[1] = "apelsin"
print("Pärast elemendi muutmist:", puuviljad)

# Kontrolli, kas väärtus eksisteerib listis
if "õun" in puuviljad:
    print("Õun on listis olemas.")
else:
    print("Õuna ei ole listis.")

# Väljasta listi pikkus
print("Listi pikkus:", len(puuviljad))

# Eemalda listist element
puuviljad.remove("banaan")
print("Pärast banaani eemaldamist:", puuviljad)
