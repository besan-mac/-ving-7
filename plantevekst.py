# En forenklet modell av hvordan en plante vokser basert på
# temperatur er som følger: Planten trenger et minimum av 5 plussgrader for å vokse. Dere
# kan regne at planten sin vekst en gitt dag er lik temperatur minus
# minimumstemperaturen. Beregn total plantevekst et gitt år.

from csv_colum import * 

def _plantevekst_dag(avg_temperatur:float, minimumstemperatur:float):
    if avg_temperatur < minimumstemperatur:
        return 0
    else:
        return avg_temperatur - minimumstemperatur

def plantevekst(år:int):
    with open('sinnes_2014_2025_med_makstemperatur.csv', 'r') as f:
        f.readline()

        total_plantevekst = 0

        for linje in f:
            data = linje.split(';')
            if data[Tid].endswith(str(år)):
                if data[Middel_temp] == "-":
                    continue
                avg_temp = float(data[Middel_temp].replace(',', '.'))
                total_plantevekst += _plantevekst_dag(avg_temp, 5)

    print(f"År: {år}")
    print(f"Total plantevekst: {total_plantevekst:.2f}")

plantevekst(2014)