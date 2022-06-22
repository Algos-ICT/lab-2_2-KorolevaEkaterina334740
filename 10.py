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


def isBST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        sp = []
        for i in range(n):
            x = list(map(int, file.readline().split()))
            sp.append(x)

        tree = []
        for i in range(len(sp)):
            tree.append(Node(sp[i][0]))

        for i in range(len(sp)):
            if sp[i][1] != 0:
                tree[i].insert_l(tree[sp[i][1] - 1])

            if sp[i][2] != 0:
                tree[i].insert_r(tree[sp[i][2] - 1])

    with open('output.txt', 'w') as file:
        if tree:
            if isBST(tree[0]):
                file.write('YES')
            else:
                file.write('NO')
        else:
            file.write('YES')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Создадим дерево и проверим его через функцию isBST. Если корень меньше либо равен любому узлу, то выводим NO, 
иначе – YES.
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
YES
'''

'''
0
YES
'''

'''
3
5 2 3
6 0 0
4 0 0
Result:
NO
'''