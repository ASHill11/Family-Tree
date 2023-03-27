from anytree import Node, RenderTree

def build_tree(data, parent=None):
    """Recursively build a tree from a nested list."""
    for item in data:
        if isinstance(item, list):
            if isinstance(item[0], str):
                node = Node(item[0], parent=parent)
                build_tree(item[1:], parent=node)
            else:
                build_tree(item, parent=parent)
        else:
            node = Node(item, parent=parent)

# Example usage:
data = ['Grandpa', ['Dad', ['Child 1', 'Child 2']], ['Uncle', ['Child 3']]]
root = Node('My Family Tree')
build_tree(data, parent=root)
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")
