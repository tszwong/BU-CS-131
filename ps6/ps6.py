# Sources Consulted: Jane, Classmate

def is_reflexive(A, R):
    for x in A:
        if not R(x, x):
            return False

    return True


def is_transitive(A, R):
    for x in A:
        for y in A:
            for z in A:
                if R(x, y) and R(y, z) and not R(x, z):
                    return False

    return True


s = {1, 2, 3}


def relation1(x, y):
    return x == y


def relation2(x, y):
    return x == y and x != 3


def relation3(x, y):
    return x >= y

def relation4(x, y):
    return (x + y) % 2 == 1


print(is_reflexive(s, relation1))  # returns True
print(is_reflexive(s, relation2))  # returns False
print(is_transitive(s,relation3))  # returns True
print(is_transitive(s,relation4))  # returns False
