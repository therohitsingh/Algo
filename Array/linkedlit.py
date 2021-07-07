class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None

    def push(self,newdata):

        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

     def printlit(self):
         temp = self.head
         while(temp):
             print(temp.data)
             temp = temp.next

if __name__ == "__main__":
    
    llist = linkedlist()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(6)

    llist.printlit()


