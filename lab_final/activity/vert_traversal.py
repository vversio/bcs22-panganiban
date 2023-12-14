from collections import defaultdict

class tree_node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def vertical_order_traversal(root):
    if not root:
        return []
    vertical_order = defaultdict(list)

    queue = [(root, 0)]

    while queue:
        node, distance = queue.pop(0)

        vertical_order[distance].append(node.data)

        if node.left:
            queue.append((node.left, distance - 1))

        if node.right:
            queue.append((node.right, distance + 1))

    sorted_distances = sorted(vertical_order.keys())
    result = []
    for distance in sorted_distances:
        result.extend(vertical_order[distance])
    return result

def print_vertical_order(output_list, reverse=False):
    for val in output_list:
        print(f"{val:^3}", end=" ")
    print()

root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
root.right.left = tree_node(6)
root.right.right = tree_node(7)
root.right.left.right = tree_node(8)
root.right.right.right = tree_node(9)

result = vertical_order_traversal(root)
print("Original order:")
print_vertical_order(result)

reversed_result = result[::-1]
print("Reversed order:")
print_vertical_order(reversed_result, True)
