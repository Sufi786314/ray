class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insertAtStart(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insertAtLast(self, data):
        new_node = Node(data)
        temp = self.start
        if not self.isEmpty():
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            else:
                temp = temp.next
        return None

    def insertAfter(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node

    def printList(self):
        temp = self.start
        while temp:
            print(temp.item, end=" --> ")
            temp = temp.next

# Create an instance of the SLL class
mylist = SLL()

# Call the insertAtStart method on the instance
mylist.insertAtStart(data=10)

# Call the printList method on the instance to display the list
mylist.printList()
