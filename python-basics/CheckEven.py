def is_even(x: int):
    return x % 2 == 0


if __name__ == "__main__":
    n = 101
    if is_even(n):
        print('True')
    else:
        print('False')
