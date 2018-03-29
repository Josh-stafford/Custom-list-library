class list:


    def __init__(this, init_node):
        this.start = Node(init_node)
        this.length = 1

    def traverse(this, show=False):
        node = this.start
        while 1:
            if node.pointer != None:
                if show:
                    print(node.data)
                node = node.pointer
            else:
                if show:
                    print(node.data)
                return node

    def findLastNode(this):
        return this.traverse()

    def show(this):
        this.traverse(show=True)

    def push(this, data):
        this.traverse().pointer = Node(data)
        this.length += 1

    def remove(this, index):
        node = this.start
        this.length -= 1

        nodeBefore = 0
        nodeAfter = 0
        if index == 0:
            this.start = node.pointer
        else:
            for i in range(0, index):
                if i+1 == index:
                    nodeBefore = node
                elif node.pointer == None and i+1 < index:
                    print('Index value out of range')
                    return

                node = node.pointer

            nodeBefore.pointer = node.pointer

    def insert(this, index, data):
        this.length += 1
        pointerToMove = 0
        toInsert = Node(data)
        node = this.start
        if index == 0:
            pointerToMove = this.start
            this.start = toInsert
            toInsert.pointer = pointerToMove
        else:
            for i in range(0, index):
                if i+1 == index:
                    pointerToMove = node.pointer
                    node.pointer = toInsert
                    toInsert.pointer = pointerToMove
                    break
                elif node.pointer == None and i+1 < index:
                    print('Index value out of range')
                    return

                node = node.pointer

    def find(this, index):
        node = this.start

        for i in range(0, index+1):
                if i == index:
                    return node
                else:
                    node = node.pointer

class Node:

    def __init__(this, data):
        this.data = data
        this.pointer = None
