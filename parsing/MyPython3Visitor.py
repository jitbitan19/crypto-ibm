from Tree import Tree
from Node import Node


class Python3Handler:
    def __init__(self) -> None:
        self.memory = {}

    def file_input(self, node: Node):
        for c in node.children:
            if c.value == "stmt":
                self.stmt(c)

    def stmt(self, node: Node):
        for c in node.children:
            if c.value == "simple_stmts":
                self.simple_stmts(c)
            else:
                self.compound_stmt(c)

    def simple_stmts(self, node: Node):
        for c in node.children:
            if c.value == "simple_stmt":
                self.simple_stmt(c)

    def simple_stmt(self, node: Node):
        for c in node.children:
            if c.value == "expr_stmt":
                self.expr_stmt(c)
            elif c.value == "del_stmt":
                self.del_stmt(c)
            elif c.value == "pass_stmt":
                self.pass_stmt(c)
            elif c.value == "flow_stmt":
                self.flow_stmt(c)
            elif c.value == "import_stmt":
                self.import_stmt(c)
            elif c.value == "global_stmt":
                self.global_stmt(c)
            elif c.value == "nonlocal_stmt":
                self.nonlocal_stmt(c)
            elif c.value == "assert_stmt":
                self.assert_stmt(c)

    def expr_stmt(self, node: Node):
        if "=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "+=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "-=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "*=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "@=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "/=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "%=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "&=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "|=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "^=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "<<=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif ">>=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "**=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        elif "//=" in node.children:
            self.memory[node.children[0]] = self.test(node.children[2])
        else:
            pass

    def test(self, node: Node):
        if len(node.children) == 1:
            return self.or_test(node.children[0])

    def or_test(self, node: Node):
        x = []
        for c in node.children:
            if c.value != "or":
                x.append(self.and_test(c))
        y = x[0]
        for i in x:
            y = y and x
        return y

    def and_test(self, node: Node):
        x = []
        for c in node.children:
            if c.value != "and":
                x &= self.not_test(c)
        return x

    def not_test(self, node: Node):
        if len(node.children) == 1:
            return self.comparision(node.children[0])
        else:
            return not self.comparision(node.children[1])

    # Only binary comparision is added
    def comparision(self, node: Node):
        if len(node.children) == 1:
            return self.expr(node.children[0])
        else:
            if "<" in node.children:
                return self.expr(node.children[0]) < self.expr(node.children[2])
            elif ">" in node.children:
                return self.expr(node.children[0]) > self.expr(node.children[2])
            elif "==" in node.children:
                return self.expr(node.children[0]) == self.expr(node.children[2])
            elif ">=" in node.children:
                return self.expr(node.children[0]) >= self.expr(node.children[2])
            elif "<=" in node.children:
                return self.expr(node.children[0]) <= self.expr(node.children[2])
            # elif '<>' in node.children:
            #     return node.children[0] <> node.children[2]
            elif "!=" in node.children:
                return self.expr(node.children[0]) != self.expr(node.children[2])
            elif "in" in node.children:
                return self.expr(node.children[0]) in self.expr(node.children[2])
            elif "is" in node.children:
                return self.expr(node.children[0]) is self.expr(node.children[2])
            elif "not in" in node.children:
                return self.expr(node.children[0]) not in self.expr(node.children[2])
            elif "is not" in node.children:
                return self.expr(node.children[0]) is not self.expr(node.children[2])

    def expr(self, node: Node):
        if len(node.children) == 1:
            self.atom_expr(node.children[0])
        else:
            # ('+' | '-' | '~')+ expr are ignored
            if "**" in node.children:
                return self.atom_expr(node.children[0]) ** self.atom_expr(
                    node.children[2]
                )
            if "*" in node.children:
                return self.atom_expr(node.children[0]) * self.atom_expr(
                    node.children[2]
                )
            if "@" in node.children:
                return self.atom_expr(node.children[0]) @ self.atom_expr(
                    node.children[2]
                )
            if "/" in node.children:
                return self.atom_expr(node.children[0]) / self.atom_expr(
                    node.children[2]
                )
            if "%" in node.children:
                return self.atom_expr(node.children[0]) % self.atom_expr(
                    node.children[2]
                )
            if "//" in node.children:
                return self.atom_expr(node.children[0]) // self.atom_expr(
                    node.children[2]
                )
            if "+" in node.children:
                return self.atom_expr(node.children[0]) + self.atom_expr(
                    node.children[2]
                )
            if "-" in node.children:
                return self.atom_expr(node.children[0]) - self.atom_expr(
                    node.children[2]
                )
            if "<<" in node.children:
                return self.atom_expr(node.children[0]) << self.atom_expr(
                    node.children[2]
                )
            if ">>" in node.children:
                return self.atom_expr(node.children[0]) >> self.atom_expr(
                    node.children[2]
                )
            if "&" in node.children:
                return self.atom_expr(node.children[0]) & self.atom_expr(
                    node.children[2]
                )
            if "^" in node.children:
                return self.atom_expr(node.children[0]) ^ self.atom_expr(
                    node.children[2]
                )
            if "|" in node.children:
                return self.atom_expr(node.children[0]) | self.atom_expr(
                    node.children[2]
                )

    # only atom is added no trailer yet
    def atom_expr(self, node: Node):
        pass

    def atom_expr(self, node: Node):
        pass

    def del_stmt(self, node: Node):
        pass

    def pass_stmt(self, node: Node):
        pass

    def flow_stmt(self, node: Node):
        pass

    def import_stmt(self, node: Node):
        pass

    def global_stmt(self, node: Node):
        pass

    def nonlocal_stmt(self, node: Node):
        pass

    def assert_stmt(self, node: Node):
        pass

    def compound_stmt(self, node: Node):
        pass
