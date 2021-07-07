def push(self,data):
    ptr1 = Node(data)
    temp = self.head

    ptr1.next = self.head

    if self.head is not None:
        while(temp.next != self.head):
            temp = temp.next
        temp.next = ptr1

        else: 
            ptr1.next = ptr1 # For the first node 
  
        self.head = ptr1    