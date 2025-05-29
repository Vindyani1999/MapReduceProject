#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = None

for row in reader:
    if not header:
        header = row
        cities = header[1:]  # Skip the datetime
        continue

    if len(row) < 2:
        continue
    date_str = row[0]
    try:
        year = date_str.split()[0].split('/')[-1]
    except IndexError:
        continue



    for i, temp_str in enumerate(row[1:]):
        if temp_str.strip():
            try:
                temp = float(temp_str)
                city = cities[i]
                print(f"{year}\t{city}\t{temp}")
            except ValueError:
                continue