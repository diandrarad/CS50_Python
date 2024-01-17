import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

rows = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
        header = rows[0].keys()
        rows = [x.values() for x in rows]
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(rows, header, tablefmt="grid"))