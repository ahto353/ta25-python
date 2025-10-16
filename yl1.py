 # kroonide -> eurode teisendaja (Python)
KURS = 15.6466  # 1 EUR = 15.6466 EEK

def teisenda_kroonidest_eurodeks(kroonid):
    eurod = kroonid / KURS
    return eurod

def main():
    try:
        s = input("Sisesta summa kroonides: ").strip().replace(',', '.')
        kroonid = float(s)
    except ValueError:
        print("Vigane sisend — palun sisesta number (näiteks 100 või 123.45).")
        return

    eurod = teisenda_kroonidest_eurodeks(kroonid)

    # Variant A: ümardatud täisarvuks
    eurod_ums_tais = round(eurod)   # round to nearest integer

    # Variant B: ümardatud kahe komakohani
    eurod_2kom = round(eurod, 2)    # round to 2 decimal places

    print(f"{kroonid} EEK on ligikaudu {eurod_ums_tais} EUR (ümardatud täisarvuks).")
    print(f"{kroonid} EEK ≈ {eurod_2kom} EUR (ümardatud 2 komakohani).")

if __name__ == "__main__":
    main()
