def print_multiplication_table(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i = i + 1


def print_multiplication_table_var2(n):
    for i in range(1, 11):
        print("%d * %d = %d" % (n, i, n*i))


if __name__ == '__main__':
    print_multiplication_table(5)
    print("\n")
    print_multiplication_table_var2(5)
