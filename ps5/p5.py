# Sources Consulted: Jane Pan, classmate
import math


def similarity1(A, B):
    both = []
    one_or_both = []
    for a in A:
        if a in B:
            both += [a]
        one_or_both += [a]
    for b in B:
         if b not in one_or_both:
             one_or_both += [b]

    length_both = len(both)
    length_one = len(one_or_both)
    score = length_both / length_one

    return score


def similarity2(A, B):
    numerator = 0
    length_a = len(A)
    for i in range(length_a):
        numerator += A[i] * B[i]

    a_square = 0
    b_square = 0
    for i in A:
        a_square += (i**2)
    for i in B:
        b_square += (i ** 2)

    denominator_a = math.sqrt(a_square)
    denominator_b = math.sqrt(b_square)
    denominator_sum = denominator_a * denominator_b

    score = numerator / denominator_sum
    return score
