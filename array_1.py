# 

# ------------------------------------------------------------

import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize_array(self.size*2)
        self.A[self.n]=item
        self.n +=1

    def __resize_array(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i]=self.A[i]
        self.A = B

    def __str__(self):
        if self.n==0:
            return None
        else:
            result = ''
            for i in range(self.n):
                result = result + str(self.A[i]) +','
            return '['+ result[:-1] +']'
        
    def __getitem__(self,index):
        if 0<=index:
            return self.A[index]
        else:
            return None
        
    def find(self,item):
        if self.n ==0:
            return None
        else:
            for i in range(self.n):
                if self.A[i]==item:
                    return i
            return None
        
    def insert_at(self,pos,item):
        if self.n ==self.size:
            self.__resize_array(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i]=self.A[i-1]
        self.A[pos]=item
        self.n +=1

    def __delitem__(self,pos):
        if self.n==0:
            return None
        else:
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n -=1

    def remove(self,item):
        if self.n ==0:
            return None
        else:
            pos = self.find(item)
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n -=1


    def clear(self):
        if self.n==0:
            return
        else:
            self.size = 1
            self.n = 0

    def pop(self):
        if self.n==0:
            return None
        else:
            print(self.size)
            print(f"This is : {self.n-1}")
            print(self.A[self.n-1])
            self.n -=1
L = MeraList()
L.append('hello')
L.append(1)
L.append(0.5)
L.append(True)
print(len(L))
print(L)
print(L[2])
L.insert_at(0,0)
print(f"tis {L.find(1)}")
L.pop()
print(L)
del L[0]
print(L)
L.remove(True)
print(L)
L.clear
print(L)



