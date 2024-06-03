from Tree import Tree
from Node import Node


class Python3Handler:
    def __init__(self) -> None:
        self.memory = {}
        self.vn = False

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
        c_val = []
        for c in node.children:
            c_val.append(c.value)
        if "=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] = y
        elif "+=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] += y
        elif "-=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] -= y
        elif "*=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] *= y
        elif "@=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] @= y
        elif "/=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] /= y
        elif "%=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] %= y
        elif "&=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] &= y
        elif "|=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] |= y
        elif "^=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] ^= y
        elif "<<=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] <<= y
        elif ">>=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] >>= y
        elif "**=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] **= y
        elif "//=" in c_val:
            self.vn = True
            x = self.test(node.children[0].children[0])
            self.vn = False
            y = self.test(node.children[2].children[0])
            self.memory[x] //= y
        else:
            self.vn = True
            y = self.test(node.children[0].children[0])
            self.vn = False
            # print(y)

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
            y = y and i
        return y

    def and_test(self, node: Node):
        x = []
        for c in node.children:
            if c.value != "and":
                x.append(self.not_test(c))
        y = x[0]
        for i in x:
            y = y and i
        return y

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
            return self.atom_expr(node.children[0])
            # other math operations
        else:
            # ('+' | '-' | '~')+ expr are ignored
            x = "a"
            y = "b"
            c_val = []
            for i in node.children:
                c_val.append(i.value)

            if "**" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x**y
            if "*" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x * y
            if "@" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x @ y
            if "/" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x / y
            if "%" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x % y
            if "//" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x // y
            if "+" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x + y
            if "-" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x - y
            if "<<" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x << y
            if ">>" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x >> y
            if "&" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x & y
            if "^" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x ^ y
            if "|" in c_val:
                x = self.expr(node.children[0])
                y = self.expr(node.children[2])
                return x | y

    # only atom is added no trailer yet
    def atom_expr(self, node: Node):
        if len(node.children) == 1:
            return self.atom(node.children[0])

    def atom(self, node: Node, vn=False):
        if len(node.children) == 1:
            x = node.children[0].value
            if x == "None":
                return None
            elif x == "True":
                return True
            elif x == "False":
                return False
            if x == "name":
                if self.vn:
                    return node.children[0].children[0].value
                else:
                    return int(self.memory[node.children[0].children[0].value])
            else:
                return int(x)

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
