from sys import maxsize 

def createstack():
    stack = []
    return stack

def isempty(stack):
    if len(stack)==0:
        print("Stack was empty")
        return stack


def push(stack,item):
    stack.append(item)  
    print(item + "Stack item is added")

def pop(stack,item):
    if (isEmpty(stack)): 
        return str(-maxsize -1) 
      
    return stack.pop()  

 def peek(stack): 
    if (isEmpty(stack)): 
        return str(-maxsize -1) # return minus infinite 
    return stack[len(stack) - 1]          

stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack") 