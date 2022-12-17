import json


def task():
    filename = "input.json"
    # считать содержимое JSON файла
    with open(filename) as f:
        json_data = json.load(f)

        x = max(json_data, key=lambda i: i["score"])

    return x  # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
