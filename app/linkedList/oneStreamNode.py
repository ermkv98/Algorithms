class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_list(node):
    while node:
        print(node),
        node = node.next
    print


def find_bottom(node):
    while node.next:
        bottom = node.next
        return bottom
    return


def add_bottom(node, bottom):
    bottom.next = node
    bottom = node
    return bottom


def find_node(node, target):
    while node.next:
        if target == node.next:
            return node
        node = node.next
    return


def cut_list(node):
    node.next = None


def find_greatest(node):
    greatest = int(node.data)
    while node.next:
        if greatest < int(node.data):
            greatest = int(node.data)
        node = node.next
    return greatest
