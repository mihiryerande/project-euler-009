# Problem 009:
#     Special Pythagorean Triplet
#
# Description:
#     A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#         a^2 + b^2 = c^2
#
#     For example,
#         3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt


def main(n):
    """
    Returns a Pythagorean triplet summing to `n`, as well as its product.

    Args:
        n (int): Natural number greater than 5

    Returns:
        Pythagorean triplet summing to `n`, and the triplet's product.

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 5

    for a in range(1, n//3):
        for b in range(a+1, (n-a)//2):
            c = n - a - b
            if sqrt(a**2 + b**2) == c:
                t = [a, b, c]
                p = a * b * c
                return t, p
    return [0, 0, 0], 0


if __name__ == '__main__':
    num = 1000
    triplet, product = main(num)
    print('Pythagorean triplet summing to {}:')
    print('  {} = {}'.format(' + '.join(map(str, triplet)), num))
    print('  {} = {}'.format(' × '.join(map(str, triplet)), product))
