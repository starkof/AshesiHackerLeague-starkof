# Candy distribution system
# Ideal for increasing the number of dentist's appointments
# by: Stephan N. Ofosuhene


def distribute(m, n):
    if not isinstance(m, int) or not isinstance(n, int):
        print('Invalid Input: Only integers are allowed')

    if n <= 0:
        return []
    if m <= 0:
        return [0]*n

    gozinta = m//n

    # list showing the number of candy received by each child
    happy_children = [gozinta]*n

    for i in range(m % n):
        happy_children[i] += 1

    print(happy_children)

    return happy_children


# print(distribute(5, 5))

if __name__ == '__main__':
    m = 5
    n = 5

    distribute(m, n)
