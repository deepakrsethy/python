def check_even_or_odd(x: int) -> str:
    if x % 2 == 0:
        return 'Even'
    return 'Odd'


print(check_even_or_odd(10))

print(check_even_or_odd(11))

print(check_even_or_odd(-10))

print(check_even_or_odd(-11))

print(check_even_or_odd(0))
