
def maximalSubarray(arr):
    sums = []
    for i in arr:
        if len(sums) == 0:
            sums.append(i)
        else:
            sums.append(max(i, i+sums[-1]))
    return sums


if __name__ == '__main__':
    cases = [[1, -3, 5, -2, 9, -8, -6, 4]]
    for case in cases:
        print('{}\n{}\n\n'.format(case, maximalSubarray(case)))
