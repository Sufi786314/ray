class Node:
    def __init__(self,prev=None ,item=None ,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start = None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insertStart(self,data):
        new_node = Node(item=data,next = self.start)
        self.start = new_node

    def insertEnd(self,data):
        if self.start is not None:
            new_node = Node(item = data)
            temp = self.start
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.start = new_node
        
    def search(self,data):
        temp = self.start
        while(temp):
            if temp.item is data:
                return temp
            temp = temp.next
        return None
    
    def insertAfter(self,temp,data):
        new_node = Node(prev=temp,item=data,next=temp.next)
        temp.next = new_node

    def printList(self):
        temp = self.start
        while(temp):
            print(temp.item,end="-->")
            temp = temp.next
mylist = DLL()
mylist.insertStart(5)
# mylist.printList()
mylist.insertEnd(10)
# mylist.printList()
mylist.insertAfter(mylist.search(5),7)
mylist.insertAfter(mylist.search(10),22)
mylist.printList()