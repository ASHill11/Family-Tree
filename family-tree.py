from anytree import Node, RenderTree


def build_tree(data, parent=None):
    """Recursively build a tree from a nested list."""
    for item in data:
        node = Node(str(item), parent=parent)
        if isinstance(item, list):
            build_tree(item, parent=node)


def print_tree(tree):
    """Print the tree chart using anytree's RenderTree function."""
    for pre, _, node in RenderTree(tree):
        print(f"{pre}{node.name}")


# Example usage:
data = ['a', ['b', ['d', 'e'], 'c'], 'f']
root = Node('root')
build_tree(data, parent=root)
print_tree(root)

