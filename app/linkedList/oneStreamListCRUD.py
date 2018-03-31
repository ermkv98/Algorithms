from oneStreamNode import *

print('creating nodes')
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2

bottom = find_bottom(node1)

print('printing node list')
print_list(node1)

print('adding node3')
bottom = add_bottom(node3, bottom)

print_list(node1)

print('adding node4')
bottom = add_bottom(node4, bottom)

print_list(node1)

print('adding node5')
bottom = add_bottom(node5, bottom)

print_list(node1)

print('looking for node 3')
node_3 = find_node(node1, node3)

print('this part will be deleted')
print_list(node_3.next)

print('cutted list')
cut_list(node_3)
print_list(node1)
