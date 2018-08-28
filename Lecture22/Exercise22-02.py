class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        pass
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


r = Node(3)
binary_insert(r, Node(1))
binary_insert(r, Node(8))
binary_insert(r, Node(2))
binary_insert(r, Node(9))

print("in order:")
in_order_print(r)

print("pre order")
pre_order_print(r)

in_order_print(1, 2, 3, 8, 9)

pre_order_print(3, 1, 8, 2, 9)
