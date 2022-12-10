def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    max_gen = (i for i in list_words)
    return len(max(max_gen))  # записать выражение-генератор


if __name__ == "__main__":
    print(task())

# задание решено