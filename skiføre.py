# Hvis vi antar at det er skiføre så lenge snødybden er minst 20cm, la brukeren
# skrive inn et årstall og regn ut for et oppgitt år hvor mange dager det var skiføre den
# skisesongen. En skisesong strekker seg fra november forrige år til mai dette året.


from datetime import datetime
from pathlib import Path

filnavn = Path(__file__).resolve().parent / "sinnes_2014_2025.csv"

aar = int(input("Skriv inn årstall: "))

startdato = datetime(aar - 1, 11, 1)
sluttdato = datetime(aar, 5, 31)

antall_skidager = 0

with open(filnavn, "r", encoding="utf-8-sig") as fil:
    for linje in fil:
        data = linje.strip().split(";")

        if len(data) < 7:
            continue

        try:
            dato = datetime.strptime(data[2].strip(), "%d.%m.%Y")
        except ValueError:
            continue

        sno = data[6].strip()

        if sno == "":
            continue

        try:
            snodybde = float(sno.replace(",", "."))
        except ValueError:
            continue

        if startdato <= dato <= sluttdato:
            if snodybde >= 20:
                antall_skidager += 1

print(f"Antall dager med skiføre: {antall_skidager}")
