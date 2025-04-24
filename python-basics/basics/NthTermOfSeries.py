"""Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively,
the problem is to find the nth term of the series.
Examples :

Input : a1 = 2,  a2 = 3,  n = 4
Output : 5
Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5.

Input : a1 = 1, a2 = 3, n = 10
Output : 19
Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.
"""


def find_nth_term(a1, a2, n):
    diff = a2 - a1
    nth_term = a2
    for i in range(2, n):
        nth_term = diff + nth_term

    return nth_term


if __name__ == '__main__':
    print(find_nth_term(2, 3, 4))
    print(find_nth_term(1, 3, 10))
