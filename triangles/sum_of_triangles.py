# Sum of triangles
# by: Stephan N. Ofosuhene

import sys


def triangles(n):
    if n < 1:
        return 0

    t = 0
    for i in range(1, n+1):
        t += (i*(i + 1))/2

    return t


if __name__ == '__main__':
    print(triangles(int(sys.argv[1])))
