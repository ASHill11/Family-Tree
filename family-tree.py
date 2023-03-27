# Make sure to pip install anytree
from anytree import Node, RenderTree


def build_tree(data, parent=None, parent_name='root'):
    """Recursively build a tree from a nested list."""
    for item in data:
        if isinstance(item, list):
            node = Node(str(item[0]), parent=parent)
            build_tree(item, parent=node, parent_name=str(item[0]))
        else:
            node = Node(str(item), parent=parent)
        if parent_name and node.parent:
            node.parent.name = parent_name


def print_tree(tree):
    """Print the tree chart using anytree's RenderTree function."""
    for pre, _, node in RenderTree(tree):
        print(f"{pre}{node.name}")


# Example usage:
data = ['Cory Davis', ['Ryan Day', ['Travis Stone', ['Robert White', ['Alan', 'Joel', 'Chris']]], 'Phillip Knowles', 'Steven Wang', 'Ivan Valdez']]
root = Node('Ben King')
build_tree(data, parent=root)
print_tree(root)

