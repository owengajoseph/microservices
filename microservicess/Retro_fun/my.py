import csv

with open("products.csv")as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["country"])