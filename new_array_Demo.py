import ctypes

class MeraList:
    def __init__(self):
        self.size=1
        self.n = 0
        # create array
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            # resize list 
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
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i])+ ','
        return '['+result[:-1]+']'
    
    def __getitem__(self,index):
        return self.A[index]
    
    def pop(self):
        if self.n ==0:
            return None
        else:
            print(self.A[self.n-1])
            self.n -=1

    def clear(self):
        if self.n ==0:
            return None
        else:
            self.size = 1
            self.n = 0

    def find(self,item):
        if self.n ==0:
            return None
        else:
            for i in range(self.n-1):
                if self.A[i]==item:
                    return i
            return None
        
    def insert_at(self,pos,item):
        if self.n == self.size:
            self.__resize_array(self.size*2)
            # Negative Looping
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
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
        if self.n==0:
            return None
        else:
            pos = self.find(item)
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n -=1 


    

L = MeraList()

L.append(10)
L.append('abc')
L.append(0.5)
L.append(True)
L.insert_at(2,25)
del L[2]
L.remove(0.5)
# L.pop()
# print(L.find('abc'))
print(L)
# print(len(L))
# print(L[-1])
