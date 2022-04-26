# Problem Set 9, Problem 6
# Sources Consulted: Jane, classmate

#  part a
def collatz_function(a):
    """which when given a positive number ai returns ai+1 according
    to the definition of the Collatz sequence"""

    if a >= 1:
        if a % 2 == 0:
            return a // 2
        else:
            return 3 * a + 1


# part b
def collatz_sequence(a):
    """which when given a positive number a returns the Collatz sequence
    (as a list) starting at a0 = a which terminates at some n where an = 1"""

    lst = [a]

    while a > 1:
        if a % 2 == 0:
            a = a // 2
            lst.append(a)
        else:
            a = 3 * a + 1
            lst.append(a)

    return lst


# part c
def smallest_int_with_collatz_length(n):
    """which on input n returns the smallest integer whose
    Collatz sequence has length at least n"""

    col_len = 0
    col_val = 0

    while True:

        if col_len < n:
            col_val += 1
            col_len = len(collatz_sequence(col_val))

        else:
            return col_val


# print(smallest_int_with_collatz_length(500))
# counterexample = 500 --> smallest_int_with_collatz_length(500) = 636331
