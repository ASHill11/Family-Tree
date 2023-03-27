from anytree import Node, RenderTree

def build_tree(data, parent=None):
    """Recursively build a tree from a nested list."""
    for i, item in enumerate(data):
        if isinstance(item, list):
            if parent is None:
                node = Node("")
            else:
                node = Node("", parent=parent)
            build_tree(item, parent=node)
        else:
            if i == 0:
                parent.name = item
            else:
                node = Node(item, parent=parent)

# Example usage:
data = ['Grandpa', ['Dad', ['Child 1', 'Child 2']], ['Uncle', ['Child 3']]]
root = Node('My Family Tree')
build_tree(data, parent=root)
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")
