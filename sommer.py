
import csv
from datetime import datetime

filename = "/Users/besanhamad/Documents/DAT120,2026/-ving-7/sinnes.csv"

year = int(input("Enter year: "))

summer_days = 0
high_summer_days = 0
tropical_days = 0

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        try:
            date = datetime.strptime(row[2], "%d.%m.%Y")
            temperature = float(row[3].replace(",", "."))

        except (ValueError, IndexError):
            continue

        if date.year == year:
            if temperature > 20:
                summer_days += 1

            if temperature > 25:
                high_summer_days += 1

            if temperature > 30:
                tropical_days += 1

print("Number of summer days:", summer_days)
print("Number of high summer days:", high_summer_days)
print("Number of tropical days:", tropical_days)
