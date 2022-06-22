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


def inOrder(root):
    global answ
    if root is None:
        return
    inOrder(root.left)
    answ += str(root.val) + ' '
    inOrder(root.right)


def preOrder(root):
    global answ
    if root is None:
        return
    answ += str(root.val) + ' '
    preOrder(root.left)
    preOrder(root.right)


def postOrder(root):
    global answ
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    answ += str(root.val) + ' '


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        sp = [list(map(int, file.readline().split())) for _ in range(n)]

        tree = [Node(x[0]) for x in sp]

        for i in range(len(sp)):
            if sp[i][1] != -1:
                tree[i].insert_l(tree[sp[i][1]])

            if sp[i][2] != -1:
                tree[i].insert_r(tree[sp[i][2]])

        with open('output.txt', 'w') as file:
            answ = ''
            inOrder(tree[0])
            file.write(f'{answ}\n')

            answ = ''
            preOrder(tree[0])
            file.write(f'{answ}\n')

            answ = ''
            postOrder(tree[0])
            file.write(f'{answ}\n')

print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Воспользуемся двоичным деревом. Расставим элементы последовательно на места, и если рассматриваемый элемент не является 
ребенком какого-либо узла, то добавим его в словарь Q, чтобы сохранить элемент в памяти и добавить его позже.
'''

'''
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1
Result:
1 2 3 4 5
4 2 1 3 5
1 3 2 5 4
'''

'''
10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1
Result:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
'''