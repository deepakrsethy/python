def swap(x, y):
    print(f"Before swapping x = {x} and y = {y}")
    temp = x
    x = y
    y = temp
    print(f"After swapping x = {x} and y = {y}")


if __name__ == '__main__':
    swap(10,20)