# Küsi kasutajalt lemmikloom
lemmikloom = input("Sisesta oma lemmikloom: ")

# Väljasta lemmiklooma esimene täht
print("Lemmiklooma esimene täht:", lemmikloom[0])

# Koosta mitmemõõtmeline list (loomade list)
loomad = [
    ["koer", "kass", "jänes"]
]

# Lisa kasutaja lemmikloom listi lõppu
loomad[0].append(lemmikloom)

# Väljasta lemmikloomade list
print("Lemmikloomade list:", loomad)

# Väljasta listi viimase elemendi viimane täht
viimane_loom = loomad[0][-1]
print("Viimase looma viimane täht:", viimane_loom[-1])
