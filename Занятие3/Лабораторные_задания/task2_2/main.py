import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename, 'r') as fi, open(output_filename, 'w') as fo:  # считать содержимое json файл input.json
        py_obj = json.load(fi)

        json.dump(py_obj, fo, indent=4, ensure_ascii=False)  # записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
