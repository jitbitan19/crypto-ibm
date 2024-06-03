from Tree import Tree
import json


with open("output/out.json", "r") as f:
    data = json.load(f)

tr = Tree()
tr.dict_to_tree(data)
tr.dfs()