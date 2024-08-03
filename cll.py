class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self,start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None
    
    def insertFirst(self,data):
        new_node = Node(data)
        if self.isEmpty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node


    def insertLast(self,data):
        new_node = Node(data,self.last)
        if self.isEmpty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node


    def search(self,data):
        if self.isEmpty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item is data:
                return temp
            temp = temp.next
            if temp.item == data:
             return temp
        return None
    
    def insertAfter(self, temp, data):
        if temp != None:
            new_node = Node(item=data, next=temp.next)
            temp.next = new_node
            if temp == self.last:
                self.last = new_node

    def printLen(self):  
        if not self.isEmpty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end="-->")
                temp = temp.next
            print(temp.item)

    def deleteFirst(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
    
    def deleteLast(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
            
    def deleteItem(self,data):
        if not self.isEmpty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                temp = self.last.next
                if temp == self.last:
                    if temp.item == data:
                        self.deleteFirst()
                else:
                    while temp != self.last:
                        if temp.next == self.last:
                            if temp.item == data:
                                self.deleteLast()
                            break
                        if temp.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
         if self.last == None:
             return CLLIterator(None)
         else:
             return CLLIterator(self.last.next)

class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        if self.current == self.start:
            raise StopIteration
        return data
    


mylist = CLL()
mylist.insertFirst(10)
mylist.insertLast(50)
mylist.insertAfter(mylist.search(10),20)
mylist.insertAfter(mylist.search(50),60)

# print("Before printing length")
mylist.printLen()
# print("After printing length")

