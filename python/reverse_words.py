
def revwords(s):
    return ' '.join(reversed(s.split()))

def inplace_revwords(s):
    s = list(s)

    end = len(s)
    for i in range(0, end // 2):
        t = s[i]
        s[i] = s[end - i - 1]
        s[end - i - 1] = t

    # in place rev each word

    return ''.join(s)




if __name__ == '__main__':
    cases = [['the quick brown fox jumps over a lazy god', 'god lazy a over jumps fox brown quick the']]
    for func in [revwords, inplace_revwords]:
        print('{}\n'.format(func.__name__))
        for input, expected in cases:
            output = func(input)
            status = 'Pass' if output == expected else 'Fail'
            print('in:  {}\nout: {}\n{}'.format(input, output, status))
        print('-' * 20)
