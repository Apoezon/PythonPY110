from itertools import count


def task():
    counter = count(100, 10)

    # TODO распечатать с столбик первые 10 чисел бесконечного итератора
    for _ in range(10):
        num = next(counter)
        print(num)
    return


if __name__ == "__main__":
    task()
