
def rotateN(arr, n):
    for i in range(n):
        arr = rotateLeft(arr)
    return arr

def rotateLeft(arr):
    s = len(arr)
    for x in range(s // 2):
        for i in range(x, s - x - 1):
            tmp = arr[x][i]
            arr[x][i] = arr[i][s - x - 1]
            arr[i][s - x - 1] = arr[s - x - 1][s - i - 1]
            arr[s - x - 1][s - i - 1] = arr[s - i - 1][x]
            arr[s - i - 1][x] = tmp
    return arr

def print2D(arr):
    for r in arr:
        print(' '.join([str(i) for i in r]))

if __name__ == '__main__':
    testCases = []

    testCases.append([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, '?'],
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
    ])

    testCases.append([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h']
    ])

    for a in testCases:
        print2D(a)
        print('\nL:')
        print2D(rotateLeft(a))
        print('\nR:')
        print2D(rotateN(a, 2))
        print()
        print()

