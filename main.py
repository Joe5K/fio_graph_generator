from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

FIO_CSV_FILENAME = "fio.csv"

x, y = [], []
total_amount = 0
with open(FIO_CSV_FILENAME, "r", encoding="utf8") as reader:
    reader.readline()
    while line := reader.readline()[:-1]:
        date, amount = line.replace("\"", "").split(";")[:2]
        x.append(datetime.strptime(date, "%d.%m.%Y"))
        
        total_amount += float(amount.replace(",", "."))
        y.append(total_amount)

plt.subplots_adjust(bottom=.12, left=.17)
plt.xlabel("Dátum")
plt.ylabel("Suma na účte")
plt.plot(x, y)
plt.show()
