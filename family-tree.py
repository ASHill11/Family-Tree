# Make sure to pip install anytree
from anytree import Node, RenderTree


def build_tree(data, parent=None):
    """Recursively build a tree from a nested list."""
    node_dict = {}
    for item in data:
        if isinstance(item, list):
            child_key = str(item)
            if child_key not in node_dict:
                node = Node('', parent=parent)
                node_dict[child_key] = node
                build_tree(item, parent=node)
        else:
            child_key = str(item)
            if child_key not in node_dict:
                node = Node(child_key, parent=parent)
                node_dict[child_key] = node


def print_tree(tree):
    """Print the tree chart using anytree's RenderTree function."""
    for pre, _, node in RenderTree(tree):
        print(f"{pre}{node.name}")


# Example usage:
data = ['Cory Davis', ['Ryan Day', ['Travis Stone', ['Robert White', ['Alan', 'Joel', 'Chris']]], 'Phillip Knowles', 'Steven Wang', 'Ivan Valdez']]
root = Node('Ben King')
build_tree(data, parent=root)
print_tree(root)

