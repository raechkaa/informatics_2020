class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size += 1
        else:
            self._add(data, self.root)

    def _add(self, data, a):
        if data > a.data:
            if a.right is None:
                a.right = Node(data)
                self.size += 1
            else:
                self._add(data, a.right)
        else:
            if a.left is None:
                a.left = Node(data)
                self.size += 1
            else:
                self._add(data, a.left)

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def _print_tree(self, a):
        if a is not None:
            self._print_tree(a.left)
            print(str(a.data))
            self._print_tree(a.right)

    def __str__(self):
        if self.root is not None:
            self._print_tree(self.root.left)
            print(str(self.root.data))
            self._print_tree(self.root.right)
        return ""

    def __iter__(self):
        current_level = [self]

        while len(current_level) > 0:
            next_level = []
            for a in current_level:
                yield a
                if a.root.left is not None and type(a) == Node:
                    next_level.append(a.root.left)
                if a.root.right is not None and type(a) == Node:
                    next_level.append(a.root.right)
            current_level = next_level


tree = BinTree()
tree.add(2)
tree.add(1)
tree.add(7)
tree.add(0)
tree.add(3)

for i in tree:
    print(i)

