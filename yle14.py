# Küsi kasutajalt failinime
failinimi = input("Sisesta failinimi (nt fail.txt): ")

# Jaga string punktide järgi
osad = failinimi.split(".")

# Väljasta laiend
if len(osad) > 1:
    print("Faili laiend on:", osad[-1])
else:
    print("Faililaiend puudub.")
failinimi = input("Sisesta failinimi (nt fail.txt): ")
osad = failinimi.split(".")

if len(osad) > 1 and osad[-1] != "":
    print("Faili laiend on:", osad[-1])
else:
    print("Faililaiend puudub.")
