class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Doubly_Linked():
    def __init__(self):
        self.head=None
    def Insert_first(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def Insert_last(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            newnode.prev=temp
            temp.next=newnode
    def Insert_after(self,pos,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        temp=self.head
        while(temp.data!=pos):
            temp=temp.next
        if(not temp.next):
            temp.next=newnode
            newnode.prev=temp
        else:
            newnode.next=temp.next
            newnode.prev=temp
            temp.next=newnode    


    def Delete_first(self):
        if(self.head is None):
            print("Linked list is Underflow")
        else:
            self.head=self.head.next
            self.head.prev=None
    def Delete_after(self,pos):
        temp=self.head
        while(temp.data!=pos):
            temp=temp.next
        if(not temp.next):
            print("Can't Delete")
        elif(not temp.next.next):
            temp.next=None
        else:
            temp=temp.next
            temp.prev.next=temp.next
            temp=None
    def Delete_last(self):
        if(self.head is None):
            print("Linked list is Underflow")
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.prev.next=None
    def Display_list(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"<----->",end=" ")
                temp=temp.next  
            print(None)  
l=Doubly_Linked()
while(1):
    print("\n=======================\n")
    print("1.Insert Node  at First\n2.Insert Node at after specified data\n3.Insert Node at Last\n4.Delete Node at First\n5.Delete Node at specified\n6.Delete Node at last\n7.Display\n8.Exit")
    print("\n========================\n")
    c=int(input("ENter your choice:"))
    if(c==1):
        data=int(input("Enter the data to be inserted into the list:"))
        l.Insert_first(data)
    elif(c==2):
        pos=int(input("Enter the data after which the node is to be inserted:"))
        data=int(input("Enter the data to be inserted into the list:"))
        l.Insert_after(pos,data)
    elif(c==3):
        data=int(input("Enter the data to be inserted into the list:"))
        l.Insert_last(data)
    elif(c==4):
        l.Delete_first() 
    elif(c==5):
        pos=int(input("Enter the data after which the node is to be deleted:"))
        l.Delete_after(pos)
    elif(c==6):
        l.Delete_last()
    elif(c==7):
        l.Display_list()
    elif(c==8):
        break
    else:
        print("Invalid Input")       

