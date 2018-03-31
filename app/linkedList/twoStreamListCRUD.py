from twoStreamNode import *

print('creating nodes')
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node2.next = node3
node3.prev = node2

top = find_top(node3)
bottom = find_bottom(node2)

print('printing node list')
print_list(node2)

print('adding node1')
top = add_top(top, node1)
print_list(node1)

print('adding node4')
bottom = add_bottom(bottom, node4)
print_list(node1)

print('deleting node2')
delete_node(node2)
print_list(node1)
