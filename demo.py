class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

class CircularLinkList:
    def __init__(self,last=None):
        self.last = last

    def isEmpty(self):
        return self.last == None
    
    def addToEmpty(self,data):
        if self.last!=None:
            return self.last
        else:
            new_node = Node(data)
            self.last = new_node
            self.last.next = self.last
            return self.last
        
    def traverse(self):
        if self.isEmpty():
            return print("Empty LinkList")
        else:
            temp = self.last.next
            while temp:
                print(temp.item,end="-->")
                temp = temp.next
                if temp == self.last.next:
                    break
    
    def addFront(self,data):
        if self.isEmpty():
            self.addToEmpty(data)
        else:
            new_node = Node(data)
            new_node.next = self.last.next
            self.last.next = new_node
            return self.last
        
    def addEnd(self,data):
        if self.isEmpty():
            self.addToEmpty(data)
        else:
            new_node = Node(data)
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
            return self.last
    
    def search(self,data):
        if self.isEmpty():
            return None
        else:
            temp = self.last.next
            while temp:
                if temp.item == data:
                    return temp
                else:
                    temp = temp.next 
                    if temp == self.last.next:
                        break
            return None
        
    def addAfter(self,temp,data):
        if self.isEmpty():
            return None
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            return self.last
        
    def deleteFront(self):
        if self.isEmpty():
            return 
        elif self.last == self.last.next:
            self.last = None
            return self.last
        else:
            self.last.next = self.last.next.next

    def deleteEnd(self):
        if self.isEmpty():
            return
        elif self.last == self.last.next:
            self.last = None
            return self.last
        else:
            temp = self.last.next
            while temp:
                if temp.next == self.last:
                    temp.next = self.last.next
                    break
                else:
                    temp = temp.next
                    if temp == self.last.next:
                        break

    def deleteMid(self,temp):
        if self.isEmpty():
            return 
        elif self.last == self.last.next:
            self.last = None
            return self.last
        else:
            traversal = self.last.next
            while traversal.next != temp:
                traversal = traversal.next
                if traversal.next == self.last.next:
                    break
            if traversal.next == temp:
                traversal.next = temp.next
           




cll = CircularLinkList()
last = cll.addToEmpty(20)
last = cll.addFront(10)
last = cll.addEnd(30)
# print(cll.search(20))
last = cll.addAfter(cll.search(20),25)
# last = cll.deleteFront()
# last = cll.deleteEnd()
last = cll.deleteMid(cll.search(20))
cll.traverse()