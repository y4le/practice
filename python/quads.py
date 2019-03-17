"""
cracking the coding interview pg 69

print all non negative integer solutions to a^3 + b^3 = c^3 + d^3
ignore permutations and x^3 + y^3 = x^3 + y^3
"""

from collections import defaultdict

def quads(max_base, exponent):
    memo = defaultdict(list)
    for i in range(max_base):
        for j in range(i):
            val = (j ** exponent) + (i ** exponent)
            memo[val].append((j, i))

    output = []
    for val, matches in memo.items():
        for a, b in matches:
            for c, d in matches:
                if a != c and b != d and a + b < c + d:
                    output.append((a, b, c, d, val))

    return output
    return sorted(output, key=lambda m: m[-1])


def print_cube_quads():
    for a, b, c, d, val in quads(1000, 3):
        print('{}^3 + {}^3 = {}^3 + {}^3 = {}'.format(a, b, c, d, val))


if __name__ == '__main__':
    print_cube_quads()
