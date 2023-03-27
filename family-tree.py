class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.name}"


def build_family_tree():
    # create the root of the tree
    grandparent = Person("Grandparent")
    # create the parents and add them as children of the grandparent
    parent1 = Person("Parent 1", grandparent)
    parent2 = Person("Parent 2", grandparent)
    grandparent.add_child(parent1)
    grandparent.add_child(parent2)
    # create the children and add them as children of the parents
    child1 = Person("Child 1", parent1)
    child2 = Person("Child 2", parent1)
    child3 = Person("Child 3", parent2)
    child4 = Person("Child 4", parent2)
    child5 = Person("Child 5", parent2)
    parent1.add_child(child1)
    parent1.add_child(child2)
    parent2.add_child(child3)
    parent2.add_child(child4)
    parent2.add_child(child5)
    # return the grandparent, which is the root of the tree
    return grandparent
