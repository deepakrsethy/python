"""
Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples:

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.


Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, but-18 has the maximum absolute value.
"""


def find_closet(n, m):
    reminder = n % m
    if reminder == 0:
        return n
    else:
        return n - reminder


if __name__ == '__main__':
    print(find_closet(13, 4))
    print(find_closet(-15, 6))
    print(find_closet(-15, 16))
