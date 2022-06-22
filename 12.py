import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.height = None


class binTree:

    def __init__(self):
        self.root = None
        self.Q = dict()

    def search(self, key):
        if key in self.Q:
            return self.Q[key]
        return None

    def insert(self, key, left, right):
        t = self.search(key)
        if t is None:
            t = node()
            t.key = key
        if left == -1:
            t.left = None
        else:
            t.left = node()
            t.left.key = left
            t.left.parent = t
        if right == -1:
            t.right = None
        else:
            t.right = node()
            t.right.key = right
            t.right.parent = t
        if self.root is None:
            self.root = t
        self.Q[key] = t
        if t.left is not None:
            self.Q[left] = t.left
        if t.right is not None:
            self.Q[right] = t.right


with open('input.txt') as file1:
    n = int(file1.readline())
    Q = [(-1, 0, 0)]
    T = binTree()
    for i in range(n):
        Q.append(tuple(map(int, file1.readline().split())))
    for i in range(1, n+1):
        T.insert(Q[i][0], Q[Q[i][1]][0], Q[Q[i][2]][0])

    if n == 0:
        print(0)
    else:
        L = list()
        for i in range(n, 0, -1):
            t = T.search(Q[i][0])
            if t.left is None:
                if t.right is None:
                    L.append(0)
                    t.height = 1
                else:
                    L.append(t.right.height)
                    t.height = 1 + t.right.height
            elif t.right is None:
                L.append(t.left.height * -1)
                t.height = 1 + t.left.height
            else:
                L.append(t.right.height - t.left.height)
                t.height = 1 + max(t.right.height, t.left.height)

        with open('output.txt', 'w') as file2:
            for j in range(n):
                file2.write(f'{L.pop()}\n')

print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
В задании класс узла содержит в себе ячейку height (высота поддерева). Она подсчитывается в основной программе. В список
L, начиная с конца входного файла (т.е. с листьев дерева), добавляем баланс поддерева. Затем выводим с конца список, 
т.е. с начала входного файла.
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
3
-1
0
0
0
0
'''