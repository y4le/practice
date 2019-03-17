"""
cracking the coding interview 17.12

convert binary search tree to doubly linked list in place
"""

class BiNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        if self == self.left or self.left and self.left.right and self.left.right == self:
            l = 'self'
        else:
            l = self.left

        if self == self.right or self.right and self.right.right and self.right.right == self:
            r = 'self'
        else:
            r = self.right
        return '{} {} {}'.format(l, self.data, r)


class BiStructure(object):
    def __init__(self, root = None):
        self.root = root

    def bi_to_ll_helper(self, node):
        print(node.data)
        if node.left:
            left = self.bi_to_ll_helper(node.left)
        else:
            left = None

        if node.right:
            right = self.bi_to_ll_helper(node.right)
        else:
            right = None

        return self.merge_lists(left, node, right)

    def bi_to_ll(self):
        self.bi_to_ll_helper(self.root)
        self.root = self.head(self.root)

    def tail(self, node):
        if node and node.right:
            return self.tail(node.right)
        return node

    def head(self, node):
        if node and node.left:
            return self.head(node.left)
        return node

    def merge_lists(self, l, m, r):
        lo = self.tail(l)
        if lo: lo.right = m
        m.left = lo

        hi = r
        if hi: hi.left = m
        m.right = hi

        if l: return l
        return m





b1 = BiNode(1)
b4 = BiNode(4)
b6 = BiNode(6)
b10 = BiNode(10)
b3 = BiNode(3, None, b4)
b9 = BiNode(9, None, b10)
b8 = BiNode(8, None, b9)
b2 = BiNode(2, b1, b3)
b7 = BiNode(7, b6, b8)
b5 = BiNode(5, b2, b7)

bs = BiStructure(b5)

