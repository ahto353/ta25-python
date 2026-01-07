# Küsi kasutajalt string
tekst = input("Sisesta string: ")

# Eemalda algusest ja lõpust tühikud
tekst = tekst.strip()

# Kontrolli tingimusi
if len(tekst) < 7:
    print("Stringis peab olema vähemalt 7 sümbolit.")
elif len(tekst) % 2 == 0:
    print("Stringi pikkus peab olema paaritu arv.")
else:
    # Muuda string listiks
    sümbolid = list(tekst)

    # Leia keskmise sümboli indeks
    kesk_indeks = len(sümbolid) // 2

    # Väljasta kolm keskmist sümbolit
    kolm_keskmist = sümbolid[kesk_indeks - 1 : kesk_indeks + 2]
    print("Kolm keskmist sümbolit:", "".join(kolm_keskmist))
