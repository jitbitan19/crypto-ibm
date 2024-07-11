from Tree import Tree
from Node import Node


class Python3Handler:
    def __init__(self) -> None:
        self.memory = {}
        self.package_lib = {}
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

    # Assignment operations
    def expr_stmt(self, node: Node):
        if len(node.children) != 1:
            val1 = node.children[1].value
            if val1 == "=":
                self.vn = True
                x = self.test(node.children[0].children[0])
                self.vn = False
                y = self.test(node.children[2].children[0])
                self.memory[x] = y
            else:
                if node.children[1].children[0].value == "+=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] += y
                if node.children[1].children[0].value == "-=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] -= y
                if node.children[1].children[0].value == "*=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] *= y
                if node.children[1].children[0].value == "@=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] @= y
                if node.children[1].children[0].value == "/=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] /= y
                if node.children[1].children[0].value == "%=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] %= y
                if node.children[1].children[0].value == "&=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] &= y
                if node.children[1].children[0].value == "|=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] |= y
                if node.children[1].children[0].value == "^=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] ^= y
                if node.children[1].children[0].value == "<<=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] <<= y
                if node.children[1].children[0].value == ">>=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] >>= y
                if node.children[1].children[0].value == "**=":
                    self.vn = True
                    x = self.test(node.children[0].children[0])
                    self.vn = False
                    y = self.test(node.children[2].children[0])
                    self.memory[x] **= y
                if node.children[1].children[0].value == "//=":
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

    # _____Testlist start
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

    # _____Testlist end

    # _____Expression handling start
    def expr(self, node: Node):
        if len(node.children) == 1:
            return self.atom_expr(node.children[0])
            # other math operations
        else:
            # ('+' | '-' | '~')+ expr are ignored
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

    # trailer not added
    def atom_expr(self, node: Node):
        if len(node.children) == 1:
            return self.atom(node.children[0])
        else:
            pass

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
                    return self.memory[node.children[0].children[0].value]
            if '"' in x:
                return x.strip('"')
            else:
                if "." in x:
                    return float(x)
                else:
                    return int(x)
        else:
            return self.test(node.children[1].children[0])

    # _____Expression handling end

    def del_stmt(self, node: Node):
        pass

    def pass_stmt(self, node: Node):
        pass

    def flow_stmt(self, node: Node):
        pass

    # import from not added
    def import_stmt(self, node: Node):
        if node.children[0].value == "import_name":
            self.import_name(node.children[0])
        else:
            self.import_from(node.children[0])

    def import_name(self, node: Node):
        exec(f"import {self.dotted_as_names(node.children[1])}")

    def import_from(self, node: Node):
        pass

    def import_as_name(self, node: Node):
        pass

    def dotted_as_names(self, node: Node):
        if len(node.children) == 1:
            return self.dotted_as_name(node.children[0])
        else:
            x = []
            for c in node.children:
                if c.value != ",":
                    x.append(self.dotted_as_name(c))
            return ",".join(x)

    def dotted_as_name(self, node: Node):
        if len(node.children) == 1:
            return self.dotted_name(node.children[0])
        else:
            x = self.dotted_name(node.children[0])  # package name
            y = self.name(node.children[2])  # package alias
            self.package_lib[y] = x
            return x

    def import_as_name(self, node: Node):
        pass

    def dotted_name(self, node: Node):
        if len(node.children) == 1:
            return self.name(node.children[0])
        else:
            x = []
            for c in node.children:
                x.append(self.name(c))
            return ".".join(x)

    def name(self, node: Node):
        return node.children[0].value

    def global_stmt(self, node: Node):
        pass

    def nonlocal_stmt(self, node: Node):
        pass

    def assert_stmt(self, node: Node):
        pass

    def compound_stmt(self, node: Node):
        pass
