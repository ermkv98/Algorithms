class Node():
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


def find_bottom(node):
    while node.next:
        bottom = node.next
        return bottom
    return


def find_top(node):
    while node.prev:
        top = node.prev
        return top
    return


def add_top(top, node):
    top.prev = node
    node.next = top
    top = node
    return top


def print_list(node):
    while node:
        print(node),
        node = node.next
    print


def add_bottom(bottom, node):
    bottom.next = node
    node.prev = bottom
    bottom = node
    return bottom


def delete_node(node):
    prev = node.prev
    next = node.next
    node.next = None
    node.prev = None
    prev.next = next
    next.prev = prev
