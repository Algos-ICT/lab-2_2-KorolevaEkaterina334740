import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.size = None


class Tree:

    def __init__(self):
        self.root = None

    def find(self, data, root):
        if root is None or data == root.val:
            return root
        if data < root.val:
            if root.left is not None:
                return self.find(data, root.left)
            return root
        if root.right is not None:
            return self.find(data, root.right)
        return root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.size = 1
        else:
            t = self.find(data, self.root)
            if t.val == data:
                return
            elif data < t.val:
                t.left = Node(data)
                t.left.parent = t
                t.left.size = 1
            else:
                t.right = Node(data)
                t.right.parent = t
                t.right.size = 1
            while t is not None:
                t.size += 1
                t = t.parent

    def treeMin(self, root):
        while root.left is not None:
            root = root.left
        return root.val

    def rightAncestor(self, root):
        if root.parent is None:
            return 0
        if root.val < root.parent.val:
            return root.parent.val
        return self.rightAncestor(root.parent)

    def next(self, data):
        if self.root is None:
            return 0
        t = self.find(data, self.root)
        f = False
        if t.val != data:
            self.insert(data)
            f = True
            t = self.find(data, self.root)
        if t.right is not None:
            res = self.treeMin(t.right)
        else:
            res = self.rightAncestor(t)
        if f:
            self.delete(data)
        return res

    def delete(self, data):
        t = self.find(data, self.root)
        if t.right is None:
            prnt = t.parent
            if t.left is not None:
                t.left.parent = prnt
            if prnt is None:
                self.root = t.left
            elif prnt.left.val == t.val:
                prnt.left = t.left
            else:
                prnt.right = t.left
        else:
            x = self.find(self.next(t.val), self.root)
            y = x.right
            prnt = x.parent
            t.val = x.val
            if x.val != t.right.val:
                x.parent.left = y
                if y is not None:
                    y.parent = x.parent
            else:
                t.right = y
                if y is not None:
                    y.parent = t
        while prnt is not None:
            prnt.size -= 1
            prnt = prnt.parent

    def kMax(self, root, k):
        if root.right is None:
            s = 0
        else:
            s = root.right.size
        if k == s + 1:
            return root.val
        if k < s + 1:
            return self.kMax(root.right, k)
        return self.kMax(root.left, k - s - 1)


file1 = open('input.txt', 'r')
n = int(file1.readline())
T = Tree()
file2 = open('output.txt', 'w')
for i in range(n):
    com, key = list(map(int, file1.readline().split()))
    if com == 1:
        T.insert(key)
    elif com == -1:
        T.delete(key)
    else:
        file2.write(f'{T.kMax(T.root, key)}\n')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Для выполнения этой задачи воспользуемся функциями, аналогичными функциям из заданий 3 (treeMin, rightAncestor, next) и 
4 (insert) (см дополнительные задачи). Дополнительно изменим функцию delete и добавим функцию kMin для поиска 𝑘-го 
максимума (аналогично поиску 𝑘-го минимума в задании 4).
'''

'''
11
+1 5
+1 3
+1 7
0 1
0 2
0 3
-1 5
+1 10
0 1
0 2
0 3
Result:
7
5
3
10
7
3
'''