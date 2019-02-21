tests = []

"""
is_palindrome('ab  c, d!  c3ba') -> True

return True if input is palindrome, ignoring any chars other than alphebetic and ignoring case
"""

def is_palindrome(s):
  start = 0
  end = len(s) - 1
  while start < end:
    start_char = s[start]
    end_char = s[end]
    if end_char < 'A' or end_char > 'Z' and end_char < 'a' or end_char > 'z':
      end -= 1
    elif start_char < 'A' or start_char > 'Z' and start_char < 'a' or start_char > 'z':
      start += 1
    elif end_char.lower() != start_char.lower():
      return False
    else:
      end -= 1
      start += 1
  return True

is_palindrome_tests = [
    [['aba'], True],
    [['        aba'], True],
    [['abc'], False],
    [['a!ba'], True],
    [['a234b63a'], True]
]

tests.append((is_palindrome, is_palindrome_tests))


"""
return k closest destinations to target

k_closest((1, 1), [(2, 2), (3, 3)], 1) -> [(2, 2)]

inputs:
  target: 2D coordinate (e.g. (2, 3))
  destinations: list(2D coordinated) (e.g. [(1, 1), (3, 5)])
  k: num closest destinations to return

output: list of k closest destinations
"""

import math

def k_closest(target, destinations, k):
    return sorted(destinations, key=lambda destination: distance(target, destination))[:k]

def distance(start, end):
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

k_closest_tests = [[
    [(1, 1), [(3, 3), (4, 4), (2, 2)], 2],
    [(2, 2), (3, 3)]
]]

tests.append((k_closest, k_closest_tests))

if __name__ == '__main__':
    for test_func, test_cases in tests:
        print('{}:'.format(test_func.__name__))
        for inp, expected in test_cases:
            output = test_func(*inp)
            if output == expected:
                print('PASS:  {}  ->  {}'.format(inp, expected))
            else:
                print('FAIL:  {}  ->  {}  !=  {}'.format(inp, output, expected))



