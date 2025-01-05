class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def display(self, level=0, prefix=""):
        print(prefix + self.name)
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child.display(level + 1, prefix + "    └── ")  
                child.display(level + 1, prefix + "    ├── ")  

root = TreeNode("Legal Documents")
wills = TreeNode("Wills")
contracts = TreeNode("Contracts")

root.add_child(wills)
root.add_child(contracts)

wills.add_child(TreeNode("Will 1"))
wills.add_child(TreeNode("Will 2"))
contracts.add_child(TreeNode("Contract 1"))
contracts.add_child(TreeNode("Contract 2"))

print("Hierarchical Representation of Legal Documents:")
root.display()
