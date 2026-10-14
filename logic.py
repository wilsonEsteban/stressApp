from models import is_leaf, count_leaves

def get_all_leaves(node, leaves_list=None):
    if leaves_list is None:
        leaves_list = []
    if is_leaf(node):
        leaves_list.append(node)
    else:
        for child in node.children:
            get_all_leaves(child, leaves_list)
    return leaves_list

def sum_scores(node):
    if is_leaf(node):
        return node.score if node.score is not None else 0
    return sum(sum_scores(child) for child in node.children)

def calculate_percentage(node):
    leaves = count_leaves(node)
    if leaves == 0:
        return 0.0
    total_score = sum_scores(node)
    return round((total_score - leaves) / (leaves * 4) * 100, 1)

def classify_level(percentage):
    if percentage < 25:
        return "Bajo"
    if percentage < 50:
        return "Moderado"
    if percentage < 75:
        return "Alto"
    return "Muy alto"

def find_highest_category(children):
    best = None
    for current in children:
        if best is None or calculate_percentage(current) > calculate_percentage(best):
            best = current
    return best