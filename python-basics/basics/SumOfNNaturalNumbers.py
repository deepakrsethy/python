def sum_of_n_natural_numbers(n):
    print(f"Sum of first {n} numbers: {int(n*(n+1)/2)}")

def sum_of_n_natural_numbers_iterative(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i +1
    print(f"Sum of first {n} numbers: {sum}")

if __name__ == '__main__':
    sum_of_n_natural_numbers(5)

    sum_of_n_natural_numbers_iterative(5)