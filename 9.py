import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()

from collections import deque


class Node:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.iter = None


class Tree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def deleteSubtree(self, val):
        if val in self.nodes:
            root = self.nodes[val]
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
            delete_list = deque()
            delete_list.append(root)
            while len(delete_list) != 0:
                node = delete_list.popleft()
                if node.left:
                    delete_list.append(node.left)
                if node.right:
                    delete_list.append(node.right)
                self.nodes.pop(node.iter)
            global file
            file.write(str(len(self.nodes)) + '\n')


if __name__ == '__main__':

    with open('input.txt') as file:
        n = int(file.readline())
        tree = Tree()
        data = []
        nodes_iter = {}
        for i in range(1, n+1):
            data.append(list(map(int, file.readline().split())))
            tree.nodes[i] = Node()
            tree.nodes[i].val = data[i - 1][0]
            tree.nodes[i].iter = i
            nodes_iter[data[i-1][0]] = i
        m = int(file.readline())
        for_delete = list(map(int, file.readline().split()))

    for i in range(1, n+1):
        if data[i-1][1] != 0:
            tree.nodes[i].left = tree.nodes[data[i-1][1]]
            tree.nodes[data[i-1][1]].parent = tree.nodes[i]
        if data[i-1][2] != 0:
            tree.nodes[i].right = tree.nodes[data[i-1][2]]
            tree.nodes[data[i-1][2]].parent = tree.nodes[i]
        if i == 1:
            tree.root = tree.nodes[i]

    with open('output.txt', 'w') as file:
        for j in for_delete:
            if j in nodes_iter:
                j = nodes_iter[j]
            else:
                j = 0
            if j in tree.nodes:
                tree.deleteSubtree(j)
            else:
                file.write(str(len(tree.nodes)) + '\n')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
В класс Tree была добавили функция deleteSubtree, которая удаляет требуемое поддерево, вершина которой является ключом,
введенным ранее.
'''

'''
6
-2 0 2
8 4 3
9 0 0
3 6 5
6 0 0
0 0 0
4
6 9 7 8
Result:
5
4
4
1
'''