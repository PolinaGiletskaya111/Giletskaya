# TODO решите задачу
import json



def task() -> float:
    with open('input.json') as f:
        json_data = json.load(f)
    multiply = [item["score"] * item["weight"] for item in json_data]
    sum_multiply = sum(multiply)
    return round(sum_multiply, 3)



print(task())
