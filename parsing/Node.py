class Node:
    def __init__(self, v) -> None:
        self.value = v
        self.children: list[Node] = []

    def add_child(self, a):
        self.children.append(a)