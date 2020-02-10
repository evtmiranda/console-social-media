import json
import csv


def write(content, path):
    file = path + "result.csv"
    keys = content[0].keys()
    with open(file, "w", encoding="utf-8", newline="") as f:
        csvWriter = csv.DictWriter(f, keys)
        csvWriter.writeheader()
        csvWriter.writerows(content)
