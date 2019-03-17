"""
cracking the coding interview 16.11

return all possible sums of exactly k shorter/longer
"""

def k_lengths(shorter, longer, k):
    output = set()
    for i in range(k+1):
        shorts = k - i
        longs = i
        length = shorts * shorter + longs * longer
        output.add(length)
    return output

if __name__ == '__main__':
    print(k_lengths(1, 10, 5))
