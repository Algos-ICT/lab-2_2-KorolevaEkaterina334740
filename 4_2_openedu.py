class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.order = None


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def insert(self, key):
        if key not in self.nodes:
            self.nodes[key] = node()
            self.nodes[key].key = key
            self.nodes[key].order = 1
            if not tree.root:
                tree.root = self.nodes[key]
            else:
                root = tree.root
                while True:
                    if key < root.key:
                        if not root.left:
                            root.left = self.nodes[key]
                            self.nodes[key].parent = root
                            break
                        else:
                            root = root.left
                    else:
                        if not root.right:
                            root.right = self.nodes[key]
                            self.nodes[key].parent = root
                            break
                        else:
                            root = root.right
                for i in self.nodes:
                    if self.nodes[i].key > self.nodes[key].key:
                        self.nodes[i].order += 1
                    elif i != key:
                        self.nodes[key].order += 1



tree = binTree()
with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        while True:
            command = f.readline()
            if command == '':
                break
            command = list(map(str, command.split()))
            key = int(command[1])
            command = command[0]
            if command == '+':
                tree.insert(key)
            else:
                for i in tree.nodes:
                    if tree.nodes[i].order == key:
                        print(tree.nodes[i].key)