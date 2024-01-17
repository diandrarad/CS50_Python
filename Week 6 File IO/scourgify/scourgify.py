import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit("Not a csv file")

output_rows = []
with open(sys.argv[1], newline='') as input_file:
    reader = csv.reader(input_file)
    next(reader) # skip header row
    for row in reader:
        name, house = row[0], row[1]
        last, first = name.split(", ")
        output_rows.append({"first": first, "last": last, "house": house})

with open(sys.argv[2], mode='w', newline='') as output_file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in output_rows:
        writer.writerow(row)