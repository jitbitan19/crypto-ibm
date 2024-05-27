e = {
    "fdsyr": 12,
    "af": 134,
}
d = {"c": e, "a": 13, "abc": 123}


class named_dict:
    def __init__(self, n, c) -> None:
        self.name = n
        self.children = c


def dict_dfs(a: dict):
    for key, value in a.items():
        if type(a[key]) != dict:
            print(value)
        else:
            dict_dfs(a[key])


def dict_bfs(a: dict):
    x = [named_dict("root", a)]
    while x.__len__():
        t = x[0]
        if type(t) == named_dict:
            if type(t.children) == dict:
                for key, value in t.children.items():
                    x.append(named_dict(key, t.children[key]))
            else:
                x.append(t.children)
            print(t.name)
        else:
            print(t)
        x.pop(0)


# dict_dfs(d)
# print(d)


class Node:
    def __init__(self, v) -> None:
        self.value = v
        self.children = []

    def add_child(self, a):
        self.children.append(a)


class Tree:
    def __init__(self) -> None:
        self.root: Node = Node("root")

    def dfs(self):
        self.__dfs(self.root)

    def bfs(self):
        a = [self.root]
        while a.__len__():
            x = a[0]
            if len(x.children) == 0:
                print(x.value)
            else:
                a = a + x.children
                print(x.value)
            a.pop(0)

    def dict_to_tree(self, data: dict, root_val: str = "root"):
        self.root = Node(root_val)
        self.__add_children(self.root, data)

    def __dfs(self, node: Node):
        for child in node.children:
            self.__dfs(child)
            print(child.value)

    def __add_children(self, node: Node, d: dict):
        for key, val in d.items():
            child = Node(key)
            node.add_child(child)
            if isinstance(val, dict):
                self.__add_children(child, val)
            elif isinstance(val, list):
                for el in val:
                    if isinstance(el, dict):
                        self.__add_children(child, el)
                    else:
                        a = Node(el)
                        child.add_child(a)
            else:
                a = Node(val)
                child.add_child(a)


tr = Tree()
tr.dict_to_tree(d)
tr.bfs()
