def sum_of_digits(n: int):
    s: str = str(n)
    sum = 0
    for i in range(len(s)):
        digit = int(s[i])
        sum = sum + digit
    return sum


if __name__ == '__main__':
    print(sum_of_digits(123456789123456789123422))
