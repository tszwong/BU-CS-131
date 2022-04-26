# Sources Consulted: Classmate(Jane Pan)
def noMoreThanOnce(x1, x2, x3):
    return not (x1 and x2) and not (x1 and x3) and not (x3 and x2)


def atLeastOnce(x1, x2, x3):
    return x1 or x2 or x3


def exactlyOnce(x1, x2, x3):
    return x1 ^ x2 ^ x3


def differentTimeSlots(x1, x2, x3, y1, y2, y3):
    return (x1 and (y2 ^ y3)) or (x2 and (y1 ^ y3)) or (x3 and (y1 ^ y2))


def isItValid(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2,
              e3, f1, f2, f3):
    return (a1 ^ a2 ^ a3) and (b1 ^ b2 ^ b3) and (c1 ^ c2 ^ c3) and (d1 ^ d2 ^ d3) and (e1 ^ e2 ^ e3) \
           and (f1 ^ f2 ^ f3) \
           and (not(a1 and b1) and not(a2 and b2) and not(a3 and b3)) \
           and (not(a1 and c1) and not(a2 and c2) and not(a3 and c3)) \
           and (not(a1 and d1) and not(a2 and d2) and not(a3 and d3)) \
           and (not(b1 and e1) and not(b2 and e2) and not(b3 and e3)) \
           and (not(c1 and e1) and not(c2 and e2) and not(c3 and e3)) \
           and (not(c1 and d1) and not(c2 and d2) and not(c3 and d3)) \
           and (not(d1 and f1) and not(d2 and f2) and not(d3 and f3)) \
           and (not(b1 and f1) and not(b2 and f2) and not(b3 and f3)) \
