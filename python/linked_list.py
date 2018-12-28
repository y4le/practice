import random

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return ' '.join([str(x) for x in self.collect(self.head)])

    def collect(self, node):
        out = []
        runner = node
        while(runner):
            out.append(runner)
            runner = runner.next
        return out

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return str(self.value)

    def addHead(self, value):
        newNode = self.Node(value)
        newNode.next = self.head
        self.head = newNode

    def add(self, value, n=None):
        newNode = self.Node(value)
        if self.head == None:
            self.head = newNode
        else:
            self.addNode(newNode, self.head, n)

    # if n passed, insert after n
    def addNode(self, node, runner, n=None):
        # print('addNode node({}) runner({}) n({})'.format(node, runner, n))
        if runner.next == None:
            runner.next = node
        elif n == 0:
            node.next = runner.next
            runner.next = node
        else:
            nextN = n
            if type(n) == int:
                nextN -= 1
            self.addNode(node, runner.next, nextN)

    def remove(self, n=None):
        self.removeNode(self.head, n)

    def removeNode(self, node, n=None):
        if node == None:
            return
        if n == 0:



if __name__ == '__main__':
    sl = SingleLinkedList()
    for i in range(20):
        newNum = random.randint(0, 100)
        sl.add(newNum)
    print(sl)

