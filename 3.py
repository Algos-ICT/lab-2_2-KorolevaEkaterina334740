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


class binTree:

    def __init__(self):
        self.root = None

    def search(self, data, root):
        if root is None or data == root.key:
            return root
        if data < root.key:
            if root.left is not None:
                return self.search(data, root.left)
            return root
        if root.right is not None:
            return self.search(data, root.right)
        return root

    def insert(self, data):
        if self.root is None:
            self.root = node()
            self.root.key = data
        else:
            t = self.search(data, self.root)
            if t.key == data:
                return
            elif data < t.key:
                t.left = node()
                t.left.key = data
                t.left.parent = t
            else:
                t.right = node()
                t.right.key = data
                t.right.parent = t

    def delete(self, data):
        if self.root is None:
            return
        if self.root.key == data:
            self.root = None
            return
        t = self.search(data, self.root)
        if data == t.key:
            if data < t.parent.key:
                t.parent.left = None
                return
            t.parent.right = None
            return

    def treeMin(self, root):
        while root.left is not None:
            root = root.left
        return root.key

    def rightAncestor(self, root):
        if root.parent is None:
            return 0
        if root.key < root.parent.key:
            return root.parent.key
        return self.rightAncestor(root.parent)

    def next(self, data):
        if self.root is None:
            return 0
        t = self.search(data, self.root)
        f = False
        if t.key != data:
            self.insert(data)
            f = True
            t = self.search(data, self.root)
        if t.right is not None:
            res = self.treeMin(t.right)
        else:
            res = self.rightAncestor(t)
        if f:
            self.delete(data)
        return res


with open('input.txt') as file:
    L = file.readlines()
    T = binTree()

for i in L:
    com, x = i.split()
    if com == '+':
        T.insert(int(x))
    else:
        print(T.next(int(x)))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Выполнение этой задачи аналогично задаче номер 2 с изменением функций search и insert, а также добавлением некоторые 
новые функций для нахождения ближайшего числа в дереве, большего заданного.
'''

'''
+ 1
+ 3
+ 3
> 1
> 2
> 3
+ 2
> 1
Result:
3
3
0
2
'''
