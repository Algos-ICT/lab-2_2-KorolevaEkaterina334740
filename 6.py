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
        if prev and root.val < prev.val:
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
            if sp[i][1] != -1:
                tree[i].insert_l(tree[sp[i][1]])

            if sp[i][2] != -1:
                tree[i].insert_r(tree[sp[i][2]])

    with open('output.txt', 'w') as file:
        if tree:
            if isBST(tree[0]):
                file.write('CORRECT')
            else:
                file.write('INCORRECT')
        else:
            file.write('CORRECT')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Для дерева запустим функцию isBST, проверяющую, является ли корень меньше, чем предыдущее значение числа. Если да, то
выведем INCORRECT, иначе – CORRECT.
'''

'''
3
2 1 2
1 -1 -1
3 -1 -1
Result:
CORRECT
'''

'''
3
1 1 2
2 -1 -1
3 -1 -1
Result:
INCORRECT
'''

'''
0
Result:
CORRECT
'''

'''
5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1
Result:
CORRECT
'''

'''
7
4 1 2
2 3 4
6 5 6
1 -1 -1
3 -1 -1
5 -1 -1
7 -1 -1
Result:
CORRECT
'''

'''
4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1
Result:
INCORRECT
'''