from sys import maxsize 

def createstack():
    stack = []
    return stack 

def isEmpty():
    if len(stack)==0:
        print("Stack is Empty")
    else:
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
        return str(-maxsize -1)  
    return stack[len(stack) - 1]    
