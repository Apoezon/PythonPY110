from itertools import count


def task():
    num = 2 ** 0  # 1
    # с помощью yield вернуть первое число
    yield num
    for i in count(1, 1):
        # с помощью yield вернуть оставшиеся степени двойки до бесконечности
        num = 2 ** i
        yield num

if __name__ == "__main__":
    numbers = task()

    for _ in range(11):
        print(next(numbers))
