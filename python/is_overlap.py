# testing sub-functions for https://www.hackerrank.com/challenges/two-pluses/problem

def plus_overlap(r1, c1, s1, r2, c2, s2):
    v1 = ((r1 - (s1 - 1), c1), (r1 + (s1 - 1), c1))
    h1 = ((r1, c1 - (s1 - 1)), (r1, c1 + (s1 - 1)))
    v2 = ((r2 - (s2 - 1), c2), (r2 + (s2 - 1), c2))
    h2 = ((r2, c2 - (s2 - 1)), (r2, c2 + (s2 - 1)))
    return rect_overlap(v1, v2) or rect_overlap(h1, h2) or rect_overlap(v1, h2) or rect_overlap(h1, v2)


def rect_overlap(r1, r2):
    tl1, br1 = r1
    tl2, br2 = r2

    if tl1[0] > br2[0] or tl2[0] > br1[0]:
        return False
    if tl1[1] > br2[1] or tl2[1] > br1[1]:
        return False
    return True

def run_tests(cases, func):
    print('=' * 50)
    print(func.__name__)
    for input, expected in cases:
        print(input)
        output = func(*input)
        if output == expected:
            print('Pass')
        else:
            print('Fail:')
            print('in:\n{}\n\nout:\n{}\n\nexpected\n{}'.format(input, output, expected))
        print('-' * 50)

plus_overlap_test_cases = [
    [[1, 1, 2, 3, 1, 2], True],
    [[2, 3, 3, 1, 1, 2], True],
    [[2, 3, 3, 1, 1, 1], False],
    [[2, 2, 3, 1, 1, 2], True],
    [[2, 2, 3, 1, 1, 1], False],
    [[1, 1, 2, 3, 2, 2], False],
    [[2, 2, 1, 2, 3, 1], False],
    [[2, 2, 2, 2, 3, 1], True],
    [[2, 2, 3, 5, 3, 3], False],
    [[2, 2, 3, 5, 2, 3], True],
    [[3, 1, 2, 4, 1, 2], True],
]

rect_overlap_test_cases = [
    [[((0, 0), (5, 5)), ((1, 1), (4, 4))], True],
    [[((0, 0), (5, 5)), ((0, 4), (8, 8))], True],
    [[((0, 0), (5, 5)), ((4, 0), (8, 8))], True],
    [[((0, 4), (8, 8)), ((0, 0), (5, 5))], True],
    [[((4, 0), (8, 8)), ((0, 0), (5, 5))], True],
    [[((0, 0), (5, 5)), ((6, 6), (8, 8))], False],
]

if __name__ == '__main__':
    run_tests(rect_overlap_test_cases, rect_overlap)
    run_tests(plus_overlap_test_cases, plus_overlap)


