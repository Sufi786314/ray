class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
            out = ""
            current = self.head.next
            while current:
                out += str(current.value) + "->"
                current = current.next
            return out[:-2]
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
         return self.head.next == None
         
    def push(self,value):
         new_node = Node(value)
         new_node.next = self.head.next
         self.head.next = new_node
         self.size +=1

    def pop(self):
         if self.isEmpty():
              raise Exception("Popping An Element from an empty Stack")
         remove = self.head.next
         self.head.next = self.head.next.next
         self.size -=1
         return remove.value
              

mera_stack = Stack()
mera_stack.push("Hello")
mera_stack.push(10)
mera_stack.push(0.2)
mera_stack.push(True)
mera_stack.pop()
mera_stack.pop()
mera_stack.pop()
mera_stack.pop()
mera_stack.pop()
print(len(mera_stack))
print(mera_stack)
     