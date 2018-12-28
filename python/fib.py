
def _fib(n):
    if n == 1 or n == 0:
        return n
    return memofib(n-1) + memofib(n-2)


def memo(func):
    mem = {}
    def memoized(*args):
        argstring = str(args)
        if argstring in mem:
            return mem[argstring]
        result = func(*args)
        mem[argstring] = result
        return result
    return memoized

memofib = memo(_fib)

def itfib(n):
    a = 0
    b = 1
    for i in range(n):
        x = a + b
        a = b
        b = x
    return a

if __name__ == '__main__':
    for case in [8, 18, 25, 50, 500, 5000]:
        print(case, itfib(case))
        # print(case, memofib(case))
