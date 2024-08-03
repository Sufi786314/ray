class Node:
    def __init__(self,item ,next = None):
        self.item = item
        self.next = next

class SingleLinkedList:
    def __init__(self,start = None):
        self.start = start

    def isEmpty(self):
        return self.start == None
    
    def addFront(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.start = new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def printLinkedList(self):
        temp = self.start
        while temp:
            print(temp.item,end="-->")
            temp = temp.next
            if temp  == None:
                break
    
    def addEnd(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.start = new_node
            return self.start
        else:
            temp = self.start
            while temp:
                if temp.next == None:
                    temp.next = new_node
                    break
                else:
                    temp = temp.next
                    if temp == None:
                        break

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
                    if temp == None:
                        break

    def addAfter(self,temp,data):
        if self.isEmpty():
            return
        else:
            new_node = Node(data,temp.next)
            temp.next = new_node  
            return self.start     
        
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
        else:
            while temp.next:
                temp = temp.next
                if temp.next.next == None:
                    temp.next = None
                    break
                if temp.next == None:
                    break

    def deleteMid(self,temp):
        if self.isEmpty():
            return 
        elif self.start.next == None:
            self.start = None
            return self.start
        else:
            traversal = self.start
            while traversal:
                traversal = traversal.next
                if traversal.next == temp:
                    traversal.next = temp.next
                    break
                if traversal.next == None:
                    break

sll = SingleLinkedList()
linkedlist = sll.addFront(10)
linkedlist = sll.addFront(1)
linkedlisst = sll.addEnd(20)
# print(sll.search(10))
linkedlisst = sll.addAfter(sll.search(10),15)
# sll.deleteFront()
# sll.deleteEnd()
sll.deleteMid(sll.search(15))
sll.printLinkedList()
