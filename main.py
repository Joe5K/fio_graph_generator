from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

FIO_CSV_FILENAME = "fio.csv"

x, y = [], []
total_amount = 0
last_date = None
cached_day_val = 0
with open(FIO_CSV_FILENAME, "r", encoding="utf8") as reader:
    reader.readline()
    while line := reader.readline()[:-1]:
        date, amount = line.replace("\"", "").split(";")[:2]
        date, amount = datetime.strptime(date, "%d.%m.%Y"), float(amount.replace(",", "."))
        total_amount += randint(-9800, 10000)
        x.append(date)
        y.append(total_amount)

plt.subplots_adjust(bottom=.12, left=.17)
plt.xlabel("Dátum")
plt.ylabel("Suma na účte")
plt.plot(x, y)
plt.show()
