#!/usr/bin/env python3

import sys
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 3:
        date, city, temp = parts
        year = date.split('-')[0]
        print(f"{year}\t{city}\t{temp}")