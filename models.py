class Node:
    def __init__(self, name, label, reverse=False, children=None):
        self.name = name
        self.label = label
        self.reverse = reverse
        self.children = children if children is not None else []
        self.answer = None
        self.score = None


def build_node(data):
    if "children" in data:
        return Node(data["name"], data["label"], children=build_children(data["children"]))
    return Node(data["name"], data["text"], reverse=data["reverse"])


def build_children(items, index=0):
    if index == len(items):
        return []
    return [build_node(items[index])] + build_children(items, index + 1)


def is_leaf(node):
    return len(node.children) == 0


def count_leaves(node):
    if is_leaf(node):
        return 1
    return count_children_leaves(node.children)


def count_children_leaves(children, index=0):
    if index == len(children):
        return 0
    return count_leaves(children[index]) + count_children_leaves(children, index + 1)