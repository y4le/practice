def is_rotated_substring(base, target):
    return target in base + base

if __name__ == '__main__':
    for input, expected in [[['abc', 'bca'], True], [['abc', 'z'], False]]:
        print('input: {}, expected: {}, output: {}'.format(input, expected, is_rotated_substring(*input)))

