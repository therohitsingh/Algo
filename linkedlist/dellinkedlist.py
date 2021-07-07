class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None

    def push(self,ndata):
        nnode = Node(ndata)
        nnode.next = self.head
        self.head = nnode


    def deletelist(self,key):
        temp = self.head

        if(temp is not None):
            if(temp.data==key):
                self.head = temp 
                temp = None
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            if(temp==None):
                return

            prev.next = temp.next
            temp = None           

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp)
            temp = temp.next               

if __name__ == "__main__":
    
    llist = linkedlist()
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.printlist()