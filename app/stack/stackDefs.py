class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_list(stack):
    while stack:
        print(stack),
        stack = stack.next
    print


def push(stack, data):
    node = Node(data)

    node.next = stack.next
    stack.next = node


def pop(stack):
    if not stack.next:
        return -1
    result = stack.next.data
    stack.next = stack.next.next
    return result


def reverse_stack(stack, new_stack):
    while stack.next:
        push(new_stack, pop(stack))
    return new_stack


def count_nodes(stack):
    count = 0
    while stack.next:
        stack = stack.next
        count += 1
    return count
