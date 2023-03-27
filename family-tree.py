from anytree import Node, RenderTree

# Define the family members
grandpa = Node("Grandpa")
dad = Node("Dad", parent=grandpa)
uncle = Node("Uncle", parent=grandpa)
child1 = Node("Child 1", parent=dad)
child2 = Node("Child 2", parent=dad)
child3 = Node("Child 3", parent=uncle)

# Print the family tree
for pre, _, node in RenderTree(grandpa):
    print(f"{pre}{node.name}")
