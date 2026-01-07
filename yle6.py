# Küsi kolm arvu kasutajalt
a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
c = float(input("Sisesta kolmas arv: "))

# Leia suurim loogikatehetega
if a >= b and a >= c:
    maksimum = a
elif b >= a and b >= c:
    maksimum = b
else:
    maksimum = c

# Väljasta tulemus
print("Suurim arv on:", maksimum)



