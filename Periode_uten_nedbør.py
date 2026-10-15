from datetime import datetime, timedelta

datoer = []

with open("sinnes_2014_2025.csv", encoding="utf-8-sig") as fil:
    next(fil)

    for linje in fil:
        data = linje.strip().split(";")

        try:
            dato = datetime.strptime(data[2], "%d.%m.%Y")
            nedbor = float(data[4].replace(",", "."))

            if nedbor == 0:
                datoer.append(dato)

        except (ValueError, IndexError):
            continue

datoer = sorted(set(datoer))

lengste_periode = 0
antall_dager = 0
startdato = None
startdato_lengst = None
sluttdato_lengst = None
forrige_dato = None

for dato in datoer:
    if forrige_dato is not None and dato == forrige_dato + timedelta(days=1):
        antall_dager += 1
    else:
        antall_dager = 1
        startdato = dato

    if antall_dager > lengste_periode:
        lengste_periode = antall_dager
        startdato_lengst = startdato
        sluttdato_lengst = dato

    forrige_dato = dato

if lengste_periode > 0:
    print("Lengste periode uten nedbør:", lengste_periode, "dager")
    print("Startdato:", startdato_lengst.strftime("%d.%m.%Y"))
    print("Sluttdato:", sluttdato_lengst.strftime("%d.%m.%Y"))
else:
    print("Ingen dager uten nedbør funnet")
