def compressString(s):
    out = []
    lastC = None
    lastCount = 0
    for c in s:
        if c == lastC:
            lastCount += 1
        else:
            if lastC:
                out.append('{}{}'.format(lastC, lastCount))
            lastCount = 1
        lastC = c
    out.append('{}{}'.format(lastC, lastCount))
    outStr = ''.join(out)
    if len(outStr) < len(s):
        return outStr
    return s


if __name__ == '__main__':
    for s in ['abcd', 'aaaaaaaaaaabcd', 'abbbccccccdadddddabbbbbbb']:
        print(s, compressString(s))
