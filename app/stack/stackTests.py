from stackDefs import *

first = 1
second = 2
third = 3
stack = Node('sentinel')
fourth = 4

push(stack, first)
push(stack, second)
push(stack, third)
push(stack, fourth)

print('stack created:')
print_list(stack)

print('poped:')
pop(stack)
print_list(stack)

print('reversed stack:')
new_stack = Node('new sentinel')
reversed_stack = reverse_stack(stack, new_stack)
print_list(reversed_stack)

print('number of nodes in first stack: {}'.format(count_nodes(stack)))
print('first stack:')
print_list(stack)

print('number of nodes in second stack: {}'.format(count_nodes(reversed_stack)))
print('second stack:')
print_list(reversed_stack)
