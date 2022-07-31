class Deque:
    def __init__(self, size):
        self.size = size
        self.a = [None for i in range(size+1)]
        self.front = -1
        self.rear = -1

    def Is_Full(self):
        return (self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1)

    def Is_Empty(self):
        return self.front == -1

    def Enqueue_Front(self, data):
        if(self.Is_Full()):
            print("Queue is Overflow")
            return -1
        elif(self.front == -1 and self.rear == -1):
            self.front =0
            self.rear = 0
        elif(self.front == 0):
            self.front = self.size-1
        else:
            self.front -= 1
        self.a[self.front] = data

    def Enqueue_Rear(self, data):
        if(self.Is_Full()):
            print("Queue is Overflow")
            return -1
        elif(self.front == -1 and self.rear == -1):
            self.front = 0
            self.rear = 0
        elif(self.rear == self.size-1):
            self.rear = 0
        else:
            self.rear += 1
        self.a[self.rear] = data

    def Dequeue_Front(self):
        if(self.Is_Empty()):
            return "Queue is Underflow"
        elif(self.front == self.rear):
            temp = self.a[self.front]
            self.front = -1
            self.rear = -1
        elif(self.front == self.size-1):
            temp = self.a[self.front]
            self.front = 0
        else:
            temp = self.a[self.front]
            self.front += 1
        return temp

    def Dequeue_Rear(self):
        if(self.Is_Empty()):
            return "Queue is Underflow"
        elif(self.rear == self.front):
            temp = self.a[self.rear]
            self.front = -1 
            self.rear = -1
        elif(self.rear == 0):
            temp = self.a[self.rear]
            self.rear = self.size-1
        else:
            temp = self.a[self.rear]
            self.rear -= 1
        return temp

    def Get_Front(self):
        if(self.Is_Empty()):
            return "Queue is Empty"
        return self.a[self.front]

    def Get_Rear(self):
        if(self.Is_Empty()):
            return "Queue is Empty"
        return self.a[self.rear]

    def Display_Queue(self):
        print("Front:", self.front)
        print("Rear:", self.rear)
        if(self.Is_Empty()):
            print("Queue is Empty")
        else:
            temp = self.front
            while(temp != self.rear):
                print(self.a[temp], end=" ")
                temp = (temp+1) % self.size
                # if(temp==self.size-1):
                #     self.temp=0
                # else:
                #     self.temp+=1
            print(self.a[temp])


size = int(input("Enter the size for Deque:"))
d = Deque(size)
while(1):
    print("\n-----------------------------------------\n")
    print("\n1.Enqueue at Front\n2.Enqueue at Rear\n3.Dequeue at Front\n4.Dequeue at Rear\n5.Get Front\n6.Get Rear\n7.Check queue empty or not\n8.Check queue is full or not\n9.Display Queue\n10.Exit")
    print("\n-----------------------------------------\n")
    c = int(input("Enter your choice(1/2/3/4/5/6/7/8/9/10):"))
    if(c == 1):
        data = int(input("Enter your data:"))
        d.Enqueue_Front(data)
    elif(c == 2):
        data = int(input("Enter your data:"))
        d.Enqueue_Rear(data)
    elif(c == 3):
        print("Dequeued front value:", d.Dequeue_Front())
    elif(c == 4):
        print("Dequeued Rear value:", d.Dequeue_Rear())
    elif(c == 5):
        print("Get front value:", d.Get_Front())
    elif(c == 6):
        print("Get Rear value:", d.Get_Rear())
    elif(c == 7):
        print("Deque is empty:", d.Is_Empty())
    elif(c == 8):
        print("Deque is full:", d.Is_Full())
    elif(c == 9):
        d.Display_Queue()
    elif(c == 10):
        break
    else:
        print("Invalid Input")
