import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = None

    def insert_l(self, val):
        self.left = val

    def insert_r(self, val):
        self.right = val


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

        else:
            x = self.find(data, self.root)
            if x.val == data:
                return
            elif data < x.val:
                x.left = Node(data)
                x.left.parent = x
            else:
                x.right = Node(data)
                x.right.parent = x

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
        x = self.find(data, self.root)
        f = False
        if x.val != data:
            self.insert(data)
            f = True
            x = self.find(data, self.root)
        if x.right is not None:
            result = self.treeMin(x.right)
        else:
            result = self.rightAncestor(x)
        if f:
            self.delete(data)
        return result

    def delete(self, data):
        x = self.find(data, self.root)
        if x.right is None:
            parent = x.parent
            if x.left is not None:
                x.left.parent = parent
            if parent is None:
                self.root = x.left
            elif parent.left.val == x.val:
                parent.left = x.left
            else:
                parent.right = x.left
        else:
            temp = self.find(self.next(x.val), self.root)
            y = temp.right
            x.val = temp.val
            if temp.val != x.right.val:
                temp.parent.left = y
                if y is not None:
                    y.parent = temp.parent
            else:
                x.right = y
                if y is not None:
                    y.parent = x


def inOrder(root):
    global sp
    if root is None:
        return
    inOrder(root.left)
    sp.append(root.val)
    inOrder(root.right)


if __name__ == '__main__':
    file1 = open('input.txt')
    file2 = open('output.txt', 'w')
    tree = Tree()
    while line := file1.readline().split():
        operator, num = line[0], int(line[1])
        if operator == '+':
            tree.insert(num)
        else:
            sp = []
            inOrder(tree.root)
            file2.write(f'{str(sp[num - 1])}\n')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Аналогично заданию 3 с изменением функции вставки и добавлением функции для поиска 𝑘-го минимального элемента.
'''

'''
+ 1
+ 4
+ 3
+ 3
? 1
? 2
? 3
+ 2
? 3
Result:
1
3
4
3
'''