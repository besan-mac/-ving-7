import matplotlib.pyplot as plt
import pandas as pd


def plot(år: int):
  data = pd.read_csv(
      "sinnes_2014_2025_med_makstemperatur.csv", on_bad_lines="skip", sep=";"
  )

  data["Tid(norsk normaltid)"] = pd.to_datetime(
      data["Tid(norsk normaltid)"], format="%d.%m.%Y", errors="coerce"
  )

  y_cols = [
      "Middeltemperatur (døgn)",
      "Nedbør (døgn)",
      "Høyeste middelvind (døgn)",
      "Snødybde",
  ]

  for col in y_cols:
    if col in data.columns:
      if data[col].dtype == "object":
        data[col] = data[col].astype(str).str.replace(",", ".").str.strip()
      data[col] = pd.to_numeric(data[col], errors="coerce")

  filtered_data = data[data["Tid(norsk normaltid)"].dt.year == år]

  filtered_data.plot(x="Tid(norsk normaltid)", y=y_cols)

  plt.xlabel("Dato")
  plt.show()


plot(2016)