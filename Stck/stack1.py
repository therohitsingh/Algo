from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print('Initial stack :- ')
print(stack)


print('Element popped from stack:-')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('/nStack after elemeents are popped:-')
print(stack) 