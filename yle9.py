# Kolmnurga liigi määramine külgede järgi

a = float(input("Sisesta esimene külg: "))
b = float(input("Sisesta teine külg: "))
c = float(input("Sisesta kolmas külg: "))

# Väike tolerants ujukomaarvude võrdlemiseks
epsilon = 1e-9

# Kontroll, kas kolmnurk saab eksisteerida
if a <= 0 or b <= 0 or c <= 0:
    print("Kolmnurga küljed peavad olema positiivsed.")
elif a + b <= c + epsilon or a + c <= b + epsilon or b + c <= a + epsilon:
    print("Selliste külgedega kolmnurk ei saa eksisteerida.")
else:
    # Kolmnurga liigi määramine
    if abs(a - b) < epsilon and abs(b - c) < epsilon:
        print("Tegu on võrdkülgse kolmnurgaga.")
    elif abs(a - b) < epsilon or abs(a - c) < epsilon or abs(b - c) < epsilon:
        print("Tegu on võrdhaarse kolmnurgaga.")
    else:
        print("Tegu on erikülgse kolmnurgaga.")
