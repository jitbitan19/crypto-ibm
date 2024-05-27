# import sys
# from antlr4 import *
# from ExprLexer import ExprLexer
# from ExprParser import ExprParser
# from Interp.VisitorInterp import VisitorInterp


# def main(argv):
#     input_stream = FileStream(argv[1])
#     lexer = ExprLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = ExprParser(stream)
#     tree = parser.start_()


# if __name__ == "__main__":
#     main(sys.argv)

# import sys
# from antlr4 import *
# from ExprLexer import ExprLexer
# from ExprParser import ExprParser
# from Interp.ListenerInterp import ListenerInterp


# def main(argv):
#     input_stream = FileStream(argv[1])
#     lexer = ExprLexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = ExprParser(stream)
#     tree = parser.start_()
#     if parser.getNumberOfSyntaxErrors() > 0:
#         print("syntax errors")
#     else:
#         linterp = ListenerInterp()
#         walker = ParseTreeWalker()
#         walker.walk(linterp, tree)


# if __name__ == "__main__":
#     main(sys.argv)

import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
import json

# from Interp.ListenerInterp import ListenerInterp
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees
from Tree import Tree
from Node import Node


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


def get_node_text(node, parser):
    if isinstance(node, TerminalNodeImpl):
        return node.getText()
    rule_name = parser.ruleNames[node.getRuleIndex()]
    children = [get_node_text(child, parser) for child in node.children]
    return {rule_name: children}


def main(argv):
    # input_stream = InputStream('print("hello world")\n')
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    # tree = parser.single_input()
    tree = parser.file_input()
    tree_dict = get_node_text(tree, parser)
    tr = Tree()
    tr.dict_to_tree(tree_dict)
    tr.bfs()
    tree_json = json.dumps(tree_dict, indent=4)
    with open("output/out.json", "w") as f:
        f.write(tree_json)


if __name__ == "__main__":
    main(sys.argv)
