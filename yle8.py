# Liigaasta kontroll

year = 2024  # Muuda siia suvaline positiivne täisarv

# Liigaasta tingimus:
# Aasta on liigaasta, kui ta jagub 400-ga või jagub 4-ga ja ei jagu 100-ga
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "on liigaasta")
else:
    print(year, "on lihtaasta")
