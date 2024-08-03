class Node:
    def __init__(self,item,prev=None ,next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DoubleCircularLinkedList:
    def __init__(self,start= None):
        self.start = start


    def isEmpty(self):
        return self.start == None

    def addFront(self,data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.prev = new_node
            new_node.next = new_node
        else:
            new_node.prev = self.start.prev
            new_node.next = self.start
            self.start.prev = new_node
            self.start.prev.next = new_node
        self.start = new_node
        return self.start


    
    
    def traverse(self):
        if self.isEmpty():
            return print("Empty LinkedList")
        else:
            temp = self.start
            if temp != None:
                print(temp.item,end="-->")
                temp = temp.next
                while temp != self.start:
                    print(temp.item,end="-->")
                    temp = temp.next
                return None
    
    def addEnd(self,data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.prev = new_node
            new_node.next = new_node
            self.start = new_node
        else:
            new_node.prev = self.start.prev
            new_node.next = self.start
            self.start.prev.next = new_node
            self.start.prev = new_node

    def search(self,data):
        if self.isEmpty():
            return None
        else:
            temp = self.start
            while temp:
                if temp.item == data:
                    return temp
                else:
                    temp = temp.next
                    if temp == self.start:
                        break
                return None
    
    def addAfter(self,temp,data):
        if self.isEmpty():
            return None
        else:
            new_node = Node(data)
            new_node.prev = temp
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next= new_node

    def deleteFront(self):
        if self.isEmpty():
            return
        elif self.start == self.start.next:
            self.start = None
            return self.start
        else:
            self.start.next.prev = self.start.prev
            self.start.prev.next = self.start.next
            self.start = self.start.next
            return self.start
        
    def deleteEnd(self):
        if self.isEmpty():
            return 
        elif self.start == self.start.next:
            self.start = None
            return self.start
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev
        
    def deleteAfter(self,temp):
        if self.isEmpty():
            return 
        elif self.start==self.start.next and self.start == temp:
            self.start = None
        else:
            traversal = self.start
            if traversal == temp:
                self.deleteFront
            elif traversal.prev == temp:
                self.deleteEnd
            else:
                while traversal:
                    if traversal == temp:
                        traversal.next.next.prev = traversal
                        traversal.next == traversal.next.next
                    traversal = traversal.next
                    if traversal == self.start:
                        break


dcll = DoubleCircularLinkedList()
last = dcll.addFront(10)
last = dcll.addEnd(30)
last = dcll.addAfter(dcll.search(10),20)
last = dcll.deleteAfter(dcll.search(20))
# last = dcll.deleteFront()
# last = dcll.deleteEnd()
dcll.traverse()

