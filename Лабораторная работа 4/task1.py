import json

# TODO решите задачу
def task() -> float:
    with open("input.json", "r") as f:
        data = json.load(f)

    totalSum = sum(item["score"] * item["weight"] for item in data if "score" in item and "weight" in item)

    return round(totalSum, 3)

print(task())
