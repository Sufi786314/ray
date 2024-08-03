class Node:

    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class SLL:

    def __init__(self,start = None):
        self.start = start

    def isEmpty(self):
        return self.start == None
    
    def insertAtStart(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insertAtLast(self,data):
        new_node = Node(data)
        temp = Node()
        if not self.isEmpty():
            temp = self.start
            while(temp.next):
                temp = temp.next
            temp.next = new_node
        
        else:
            self.start = new_node
        
    def search(self,data):
        temp = Node()
        temp = self.start
        while(temp):
            if temp.item == data:
                return temp
            else:
                temp = temp.next
            return None
    
    def insertAfter(self,temp,data):
        if temp is not None:
            new_node = Node(data,temp.next)
            temp.next = new_node

    def printList(self):
        # temp = Node()
        temp = self.start
        while(temp):
            print(temp.item,end = "-->>")
            temp = temp.next
            if temp == None:
                print("Empty")
            if temp.next == None:
                break

    def deleteFront(self):
        if self.isEmpty():
            return
        else:
            self.start = self.start.next

    def deleteEnd(self):
        temp = self.start
        if self.isEmpty():
            return
        elif temp.next == None:
            self.start = None
            return self.start
        else:
            while temp:
                if temp.next.next == None:
                    temp.next = None
                    break
                if temp.next == None:
                    break


mylist = SLL()
mylist.insertAtStart(data = 10)
# mylist.insertAfter(mylist.search(10),20)
# mylist.insertAfter(mylist.search(20),30)
mylist.deleteEnd()
mylist.printList()