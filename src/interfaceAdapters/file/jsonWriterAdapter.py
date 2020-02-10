import json


def write(content, path):
    file = path + "result.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
