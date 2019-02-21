
def zero_rc(arr):
    rows = [False] * len(arr)
    cols = [False] * len(arr[0])
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            is_zero = arr[r][c] == 0
            rows[r] = rows[r] or is_zero
            cols[c] = cols[c] or is_zero

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if rows[r] or cols[c]:
                arr[r][c] = 0

    return arr

tests = [[
    [[1, 1, 0],
     [1, 1, 1],
     [1, 1, 1]],
    [[0, 0, 0],
     [1, 1, 0],
     [1, 1, 0]],
    ], [
    [[1, 1, 0],
     [1, 0, 1],
     [1, 1, 1]],
    [[0, 0, 0],
     [0, 0, 0],
     [1, 0, 0]],
    ]]

if __name__ == '__main__':
    for input, expected in tests:
        output = zero_rc(input)
        if output == expected:
            print('Success')
        else:
            print('Fail')
            print(input)
            print(expected)
            print(output)
