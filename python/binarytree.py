import random

class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __eq__(self, other):
            if type(other) == self.__class__:
                return self.value == other.value
            else:
                return self.value == other

        def __lt__(self, other):
            if type(other) == self.__class__:
                return self.value < other.value
            else:
                return self.value < other

        def __gt__(self, other):
            if type(other) == self.__class__:
                return self.value > other.value
            else:
                return self.value > other

        def __repr__(self):
            return str(self.value or '_')

    def insert(self, value):
        newNode = self.Node(value)
        if not self.root:
            self.root = newNode
        else:
            self._insertHelper(self.root, newNode)

    def _insertHelper(self, oldNode, newNode):
        if newNode < oldNode:
            if oldNode.left == None:
                oldNode.left = newNode
            else:
                self._insertHelper(oldNode.left, newNode)
        else:
            if oldNode.right == None:
                oldNode.right = newNode
            else:
                self._insertHelper(oldNode.right, newNode)

    def remove(self, value):
        self.root = self._removeHelper(self.root, value)

    def _removeHelper(self, node, toRemove):
        if node == None:
            return None

        if node > toRemove:
            node.left = self._removeHelper(node.left, toRemove)
            return node
        elif node < toRemove:
            node.right = self._removeHelper(node.right, toRemove)
            return node
        else:
            if node.left == None and node.right == None:
                node = None
                return node
            if node.left == None:
                node = node.right
                return node
            if node.right == None:
                node = node.left
                return node

            minRight = self.findMin(node.right)
            node.value = minRight.value
            node.right = self._removeHelper(node.right, minRight.value)
            return node


    def findMin(self, node):
        if node.left == None:
            return node
        return self.findMin(node.left)

    def inorder(self):
        return self._inorderHelper(self.root)

    def _inorderHelper(self, node):
        if node == None:
            return []
        return self._inorderHelper(node.left) + [node.value] + self._inorderHelper(node.right)


    def __repr__(self, node = None):
        if not node:
            node = self.root

        queue = [(node, 0, 0)]
        levels = []
        while queue:
            cur, depth, horiz = queue.pop(0)
            if len(levels) <= depth:
                levels.append(['_' for i in range(2 ** depth)])

            levels[depth][horiz] = cur
            if cur.left:
                queue.append((cur.left, depth + 1, horiz * 2))
            if cur.right:
                queue.append((cur.right, depth + 1, horiz * 2 + 1))

        maxChar = 3
        width = (2 ** (len(levels) - 1)) * maxChar

        out = []
        for l in range(len(levels)):
            level = levels[l]
            out.append(''.join([str(i).center(maxChar * (2**(len(levels) - l))) for i in level]).center(width))

        return '\n\n'.join(out)





def randTree(size=5):
    btree = BinaryTree()
    for i in range(size):
        btree.insert(random.randint(0, 100))
    return btree


if __name__ == '__main__':
    bt = randTree(7)
    print(bt)
    print(bt.inorder())

