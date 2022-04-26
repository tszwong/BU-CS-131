# Sources Consulted: Jane, Classmate

def are_parts_nonoverlapping(p):

    for x in p:
        for y in p:
            if x != y:
                for i in x:
                    if i in y:
                        return False

    return True


def do_parts_contain_element(x, p):

    for i in p:
        if x in i:
            return True

    return False


def do_parts_cover_set(s, p):

    for i in s:
        if do_parts_contain_element(i, p) == False:
            return False

    return True

def do_parts_have_nothing_extra(s, p):

    for i in p:
        for x in i:
            if (x in s) == False:
                return False

    return True


def is_partition(s, p):
    if do_parts_have_nothing_extra(s, p) == True and do_parts_cover_set(s, p) == True \
            and are_parts_nonoverlapping(p) == True:
        return True
    else:
        return False
