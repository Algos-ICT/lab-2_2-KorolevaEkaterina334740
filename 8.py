import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert_l(self, val):
        self.left = val

    def insert_r(self, val):
        self.right = val


def treeHeight(root):
    if root.val is None:
        return 0
    sp = []
    sp.append(root)
    height = 0
    while True:
        nodeCount = len(sp)
        if nodeCount == 0:
            return height
        height += 1
        while nodeCount > 0:
            node = sp[0]
            sp.pop(0)
            if node.left is not None:
                sp.append(node.left)
            if node.right is not None:
                sp.append(node.right)
            nodeCount -= 1


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        sp = [list(map(int, file.readline().split())) for _ in range(n)]

    tree = [Node(x[0]) for x in sp]

    for i in range(n):
        if sp[i][1] != 0:
            tree[i].insert_l(tree[sp[i][1] - 1])

        if sp[i][2] != 0:
            tree[i].insert_r(tree[sp[i][2] - 1])

    with open('output.txt', 'w') as file:
        if tree:
            file.write(str(treeHeight(tree[0])))
        else:
            file.write('0')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
В этом задании каждый узел будет содержать дополнительную ячейку deep – глубину узла. Глубины всех листьев дерева мы 
будем добавлять в массив, максимум из которого и будет высотой дерева.
'''

'''
6
-2 0 2
8 4 3
9 0 0
3 6 5
6 0 0
0 0 0
Result:
4
'''