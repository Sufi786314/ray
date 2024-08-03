class Node:
    def __init__(self,prev = None,item=None,next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DoubleLinkedList:
    def __init__(self,start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None
    
    def addFront(self,data):
        new_node = Node(item = data)
        if self.isEmpty():
            self.start = new_node
        else:
            self.start.prev = new_node
            new_node.next = self.start
            self.start = new_node

    def PrintLinkedList(self):
        temp = self.start
        if self.isEmpty():
            return print("Empty Linked List")
        while temp:
            print(temp.item,end="-->")
            temp = temp.next
            if temp == None:
                break

    def addEnd(self,data):
        new_node = Node(item  = data)
        if self.isEmpty():
            self.start = new_node
            return self.start
        else:
            temp = self.start
            while temp:
                if temp.next == None:
                    new_node.prev = temp
                    temp.next = new_node
                    break
                temp = temp.next   
                if temp == None:
                    break        

    def search(self,data):
        if self.isEmpty():
            return self.start
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
            new_node = Node(item=data)
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node

    def deleteFront(self):
        if self.isEmpty():
            return 
        else:
            self.start = self.start.next
            self.start.prev = None
            
    def deleteEnd(self):
        if self.isEmpty():
            return
        else:
            temp = self.start
            while temp:
                if temp.next.next == None:
                    temp.next = None
                    break
                else:
                    temp = temp.next
                    if temp == None:
                        break
                    
    def deleteAfter(self,temp):
        if self.isEmpty():
            return 
        else:
           temp = temp.prev 
           temp.next = temp.next.next
           temp.prev = temp

dll = DoubleLinkedList()
linkedlist = dll.addFront(10)
linkedlist = dll.addFront(20)
linkedlist = dll.addEnd(30)
linkedlist = dll.addAfter(dll.search(10),15)
# dll.deleteFront()
# print(dll.search(10))
# dll.deleteEnd()
dll.deleteAfter(dll.search(10))
dll.PrintLinkedList()