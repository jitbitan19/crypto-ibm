# Generating Lexer-Parser
Using ANTLR to generate the lexer and parser from the [grammar files for Python3](https://docs.python.org/3/reference/grammar.html) (explained below)

## Setup the system variables and alias

Run the following in the terminal (replace the **path-to-the-jar-file** with the path of the actual runtime)
```
% export CLASSPATH=".:<path-to-the-jar-file>:$CLASSPATH"

% alias antlr4='java -Xmx500M -cp "<path-to-the-jar-file>:$CLASSPATH" org.antlr.v4.Tool'

% alias grun='java -Xmx500M -cp "<path-to-the-jar-file>:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

## Compiling the grammar file
Compile the .g4 files, namely ``Python3Parser.g4`` and ``Python3Lexer.g4`` with the flag `-Dlanguage=Python3` (to compile for a python runtime except) as explained

```
% antlr4 -Dlanguage=Python3 Python3Lexer.g4
% antlr4 -Dlanguage=Python3 Python3Parser.g4
```

# Parsing Python files
Use a Python script to provide the `Python3lexer.py` and `Python3Parser.py` with a Python runtime in order to parse any file with the specified grammar.

`Python3ParserBase.py` and `Python3ParserBase.py` are also required for tokeisation and parsing the same. Scripts are provided for the same [Python3ParserBase.py](./Python3ParserBase.py) and
[Python3LexerBase.py](./Python3LexerBase.py)

## Driver Script
Here, a `driver.py` script is used to parse the files. The same is explained below
```
import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

if __name__ == "__main__":
    main(sys.argv)
```
```
% python3 driver.py input.py
```

The flow is explained such
* The `input.py` is parsed as an input to the driver script, and a `FileStream` object is generated
* Lexer tokens are generated from `FileStream` using `Python3Lexer.py` (generated during compilation of the Python3Lexer.g4)
* The token stream is provided into the parser file, namely `Python3Parser`
* An `AST` or Abstract Syntax Tree is generated at the end, which is processed further

## Generating a JSON file
The following script transforms the a `antlr4.tree.Tree` object into a more manageable Python Dictionary structure.
```
def tree_to_dict(tree, parser):
    if tree.getChildCount() == 0:  # Leaf node
        return tree.getText()
    children = [
        tree_to_dict(tree.getChild(i), parser) for i in range(tree.getChildCount())
    ]
    node_name = (
        parser.ruleNames[tree.getRuleIndex()]
        if hasattr(tree, "getRuleIndex")
        else str(tree)
    )
    return {node_name: children}
```
```
def get_node_text(node, parser):
    if isinstance(node, TerminalNodeImpl):
        return node.getText()
    rule_name = parser.ruleNames[node.getRuleIndex()]
    children = [get_node_text(child, parser) for child in node.children]
    return {rule_name: children}
```
Once the Python dictionary is generated, a JSON file can be easily generated, as explained
```
tree_dict = get_node_text(tree, parser)
tree_json = json.dumps(tree_dict, indent=4)
with open("out.json", "w") as f:
    f.write(tree_json)
```

# JSON to Tree
Going through the generated JSON, a common pattern is observed: there are __list of dictionaries__ and __dictionary of lists__ and also __dictionary of strings__. Thus, generating a tree from the such a JSON file can be done using the design perspectives mentioned below (pseudocode)
```
def fn(node, data):
    for key,val in data:
        child = Node(key)
        if val is_instance dict:
            fn(child, val)
        if val is_istance list:
            for el in list:
                if el is_instance dict:
                    fn(child, el)
                else:
                    child.add(Node(el))
        if val is_instance str:
            child.add(Node(el))
```

A `Tree` class is written following the above pseudocode and is implemented using `Node` class. Both files (.py) are attached [Tree](./Tree.py) [Node](./Node.py).

A `dict_to_tree` method is also added to the tree class for handling the `antlr4.tree.Tree` into a Tree data structure in Python.

# Tree Traversal
Two additional methods are namely `dfs` and `bfs` for __Depth First Search__ and __Breadth First Search__ respectively.

## DFS
The Depth First Search can be implemented using the following logic
```
def dfs(root_node: Node):
    for every_child in node.children:
        dfs(every_child)
        print(every_child.name)
```
Implementation in Python
```
def dfs(self):
    self.memory = ""
    self.__dfs(self.root)
    with open("out.txt", "w") as f:
        f.write(self.memory)

def __dfs(self, node: Node):
    for child in node.children:
        self.__dfs(child)
        self.memory += child.value + "\n"
        print(child.value)
```
## BFS
Breadth First search can be implemented using the following design strategy.
```
def bfs(root_node: Node):
    a = queue<Node>
    while (a.is_not_empty()):
        x = a.top()
        a.push(x.children)
        print(x.value)
```

Implementation in Python

```
def bfs(self):
    a = [self.root]
    self.memory = ""
    while a.__len__():
        x = a[0]
        a = a + x.children
        print(x.value)
        self.memory += x.value + "\n"
        a.pop(0)
    with open("out.txt", "w") as f:
        f.write(self.memory)
```

# Example parsing
A simple hello world script is written and Python and is parsed using the above instructions. The DFS and BFS outputs are the following

```
python3 driver.py input.py
```

## DFS Output
```
print
name
atom
(
"Hello world"
atom
atom_expr
expr
comparison
not_test
and_test
or_test
test
argument
arglist
)
trailer
atom_expr
expr
comparison
not_test
and_test
or_test
test
testlist_star_expr
expr_stmt
simple_stmt
simple_stmts
stmt
<EOF>
file_input
```

## BFS Output
```
root
file_input
stmt
<EOF>
simple_stmts
simple_stmt
expr_stmt
testlist_star_expr
test
or_test
and_test
not_test
comparison
expr
atom_expr
atom
trailer
name
(
arglist
)
print
argument
test
or_test
and_test
not_test
comparison
expr
atom_expr
atom
"Hello world"
```

Thank you
