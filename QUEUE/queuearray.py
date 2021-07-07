class Queue:

    def __init__(self,c):

        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    def queueEnqueue(self,data):

        if(self.capacity == self.rear):
            print("Queue is full")

        else:
            self.queue.append(data)
            self.rear += 1 

    def queueDequeue(self):

        if(self.front == self.rear):
            print("Queue is Empty")
        else:
            self.queue.pop(0)  
            self.rear -= 1  

    def queuedisplay(self):

        if(self.front == self.rear):
            print("Queue is Empty")
        for i in self.queue:
            print(i,"<--",end = '')

    def queueFront(self):
        if(self.front == self.rear):
            print("Queue is Empty")
        print('Front Element is:',self.queue[self.front]) 

 if __name__=='__main__':

     q = Queue(4)

     q.queuedisplay()
                           
