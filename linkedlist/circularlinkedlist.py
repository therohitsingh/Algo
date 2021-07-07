def push(self,data):
    nnode = Node(data)
    temp = self.head

    nnode.next = self.head

    if self.head is not None:
        while(temp.next != self.head):
            temp = temp.next
        temp.next = nnode

        else:
            nnode.next = nnode
                