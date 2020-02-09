import csv

def read(filePath):
    rows = []

    with open(filePath, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        
        for row in content:
            rows.append(row)

    return rows