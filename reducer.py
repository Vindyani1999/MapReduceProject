#!/usr/bin/env python3
import sys
current_year = None
max_temp = float('-inf')
hottest_city = None

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue
    year, city, temp_str = parts
    try:
        temp = float(temp_str)
    except ValueError:
        continue

    if year != current_year:
        # Print the hottest city for the previous year before moving on
        if current_year:
            print(f"{current_year}\t{hottest_city}\t{max_temp}")
        current_year = year
        max_temp = temp
        hottest_city = city
    else:
        # Update if found a hotter temperature for the same year
        if temp > max_temp:
            max_temp = temp
            hottest_city = city

# Print the hottest city for the last year
if current_year:
    print(f"{current_year}\t{hottest_city}\t{max_temp}")