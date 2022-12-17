INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:  # TODO открыть указатель на файл
        for string in file:  # TODO файл является итератором, который работает с циклом for в построчном режиме
            print(string, end='')

if __name__ == "__main__":
    task()
