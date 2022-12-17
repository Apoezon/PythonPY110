INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r', encoding='utf-8') as fi, open(OUTPUT_FILE, 'w', encoding='utf-8') as fo: # перезаписать содержимое одного файла в другой
        for line in map(str.upper, fi):
            fo.write(line)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
