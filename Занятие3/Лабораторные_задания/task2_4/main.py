import json


def task():
    filename = "input.json"
    key = 'contains_improvement_appeals'
    # считать содержимое JSON файла
    with open(filename) as f:
        json_data = json.load(f)
        # print(json_data)

        gen_exr = [i[key] for i in json_data]  # записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals

    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
