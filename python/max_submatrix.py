

class DpSum(object):
    def __init__(self, arr):
        self.arr = arr
        self.height = len(arr)
        self.width = len(arr[0])
        self.memo = [[0 for i in range(len(row))] for row in arr]
        self.populate_memo(arr)

    def __str__(self):
        arrstr = self.stringify_arr_rows(self.arr)
        memostr = self.stringify_arr_rows(self.memo)

        rows = ['{} <|> {}'.format(a, m) for a, m in zip(arrstr, memostr)]

        rows.append('array <' + '-' * 30 + '> memo')

        return '\n'.join(rows)

    def stringify_arr_rows(self, arr):
        return [''.join([str(i).center(5) for i in row]) for row in arr]

    def print_arr(self, arr):
        print('\n'.join(self.stringify_arr_rows(arr)))

    def populate_memo(self, arr):
        for r in range(self.height):
            for c in range(self.width):
                self.memo[r][c] = self.get_memo(r-1, c) + \
                self.get_memo(r, c-1) - \
                self.get_memo(r-1, c-1) + \
                arr[r][c]

    def get_memo(self, r, c):
        if r < 0 or r > self.height or c < 0 or c > self.width:
            return 0
        return self.memo[r][c]

    def sum(self, r1, c1, r2, c2, do_print=False):
        assert(r1 < r2 and c1 < c2)
        r1 -= 1
        c1 -= 1
        if do_print:
            print('sum ({}, {} - {}, {})'.format(r1+1, c1+1, r2, c2), self.get_memo(r2, c2), self.get_memo(r1, c2), self.get_memo(r2, c1), self.get_memo(r1, c1))
        return self.get_memo(r2, c2) - \
            self.get_memo(r1, c2) - \
            self.get_memo(r2, c1) + \
            self.get_memo(r1, c1)

    def square(self, r, c, length):
        r2 = r + length
        c2 = c + length
        if r2 >= self.height or c2 >= self.width:
            return None
        return self.sum(r, c, r2, c2)

    def max_square(self):
        max_sum = -9999999
        max_square = (-1, -1, -1)
        for r in range(self.height):
            for c in range(self.width):
                length = 1
                while r + length < self.height and c + length < self.width:
                    total = self.square(r, c, length)
                    if total > max_sum:
                        max_sum = total
                        max_square = (r, c, length)
                    length += 1
        return max_square

    def subarray(self, r1, c1, r2, c2):
        return [[i for i in row[c1:c2+1]] for row in self.arr[r1:r2+1]]

    def max_subarray(self):
        square = self.max_square()
        return self.subarray(square[0], square[1], square[0] + square[2], square[1] + square[2])

test_arr = [
    [-1, 2, 6, -8, 9],
    [6, 1, 3, -4, 5],
    [-9, 2, 5, 6, -4],
    [5, 8, 4, -7, 8],
    [2, 5, 3, 2, 6]
]

test_arr_2 = [
    [1, -2, 4],
    [-7, 5, 6],
    [-2, -12, 3]
]

test_arrays = [test_arr, test_arr_2]

if __name__ == '__main__':
    for a in test_arrays:
        dp = DpSum(a)
        print('-'*50)
        print(dp)
        print('-'*50)
        dp.print_arr(dp.max_subarray())

