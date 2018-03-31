from oneStreamNode import *

print('creating nodes')
node1 = Node(1)
node2 = Node(23)
node3 = Node(39)
node4 = Node(14)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('printing node list')
print_list(node1)

print('finding greatest in all nodes')
greatest = find_greatest(node1)
print(greatest)

print('finding greatest in node 5')
greatest = find_greatest(node5)
print(greatest)

print('finding greatest in node 4')
greatest = find_greatest(node4)
print(greatest)

print('finding greatest in node 3')
greatest = find_greatest(node3)
print(greatest)

print('finding greatest in node 2')
greatest = find_greatest(node2)
print(greatest)
