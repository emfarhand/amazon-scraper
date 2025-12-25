import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import csv
import time

from include.config import BASE_URL, HEADERS, QUERY, DELAY
from lib.amazon_parser import parse_products

output_file = "data/raw/dt=2025-12-23/amazon_oil.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["title", "rating", "review_count"]
    )
    writer.writeheader()

    for page in range(1, 6):
        print(f"Scraping page {page}")

        params = {
            "k": QUERY,
            "page": page
        }

        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        products = parse_products(response.text)

        for p in products:
            writer.writerow(p)

        time.sleep(DELAY)

print("Done.")
