def printNthFromLast(self, n): 
        temp = self.head # used temp variable 
          
        length = 0
        while temp is not None: 
            temp = temp.next
            length += 1
          
        # print count  
        if n > length: # if entered location is greater  
                       # than length of linked list 
            print('Location is greater than the' +
                         ' length of LinkedList') 
            return
        temp = self.head 
        for i in range(0, length - n): 
            temp = temp.next
        print(temp.data) 