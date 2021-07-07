def search(self,x):
    current = self.head

    while current!=None:
        if(current.data == x):
            return True

        current = current.next
    return False        


