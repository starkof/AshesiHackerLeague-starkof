# Finding triplet question marks
# by: Stephan N. Ofosuhene


def is_int(ch):
    try:
        int(ch)
        return True
    except ValueError:
        return False

def joker(string):
    ints = []
    buffer = ''
    qcount = 0

    for i in string:
        buffer += i
        if is_int(i):
            ints.append(int(i))
        elif i == '?':
            qcount += 1

        if len(ints) == 2:
            if sum(ints) == 10:
                if qcount == 3:
                    return True
            ints = []
            buffer = ''
            qcount = 0

    return False


print(joker('fslien3???0sd6???4lkj'))
