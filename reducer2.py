#!/usr/bin/env python3

import sys

current_year = None
max_temp = float('-inf')
hottest_city = ""

for line in sys.stdin:
    year, city, temp = line.strip().split("\t")
    temp = float(temp)

    if current_year == year:
        if temp > max_temp:
            max_temp = temp
            hottest_city = city
    else:
        if current_year:
            celsius = max_temp - 273.15
            print(f"{current_year}\t{hottest_city}\t{celsius:.2f} °C")
        current_year = year
        max_temp = temp
        hottest_city = city

# print last year
if current_year:
    celsius = max_temp - 273.15
    print(f"{current_year}\t{hottest_city}\t{celsius:.2f} °C")