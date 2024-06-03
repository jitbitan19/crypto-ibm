from Node import Node


class Tree:
    def __init__(self) -> None:
        self.root: Node = Node("root")
        self.memory = ""

    def dfs(self, mode="all"):
        self.memory = ""
        if mode == "all":
            self.__dfs(self.root)
        else:
            self.__dfs_leaf(self.root)
        with open("output/out.txt", "w") as f:
            f.write(self.memory)

    def dfs_leaf(self):
        self.memory = ""
        self.__dfs_leaf(self.root)
        with open("output/out.txt", "w") as f:
            f.write(self.memory)

    def bfs(self):
        a = [self.root]
        self.memory = ""
        while a.__len__():
            x = a[0]
            a = a + x.children
            print(x.value)
            self.memory += x.value + "\n"
            a.pop(0)
        with open("output/out.txt", "w") as f:
            f.write(self.memory)

    def dict_to_tree(self, data: dict, root_val: str = "root"):
        self.root = Node(root_val)
        self.__add_children(self.root, data)

    def __dfs(self, node: Node):
        # if node.children.__len__() == 0:
        #     print(node.value)
        #     return
        for child in node.children:
            self.__dfs(child)
            self.memory += child.value + "\n"
            print(child.value)

    def __dfs_leaf(self, node: Node):
        if node.children == []:
            print(node.value)
            return
        for child in node.children:
            self.__dfs_leaf(child)
            self.memory += child.value + "\n"

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
