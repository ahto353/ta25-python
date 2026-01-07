# Antud tekst
tekst = "Tere! Kuidas sul läheb?"

# Kõik täishäälikud
taishaalikud = "aeiouõäöüAEIOUÕÄÖÜ"

# Loendur täishäälikute arvuks
loendur = 0

# Tsükkel iga tähemärgi läbi
for t in tekst:
    if t in taishaalikud:
        loendur += 1

print("Täishäälikute arv:", loendur)
