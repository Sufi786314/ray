# # # list can be modified but tuples it can not be modified 
# # ray_list = []
# # # print(ray_list)
# # ray_tuple = ()
# # # ray_list.append("Ray")
# # ray_list.append(20)
# # # ray_list.append(0.5)
# # ray_list.insert(3,20)
# # # ray_list.append(True)
# # ray_list.append(10)
# # ray_list.append(40)

# # # ray_list.remove(20)
# # # ray_list2=ray_list.copy()
# # # ray_list.pop()
# # # print(ray_list.index("Ray"))
# # # print(ray_list.count(20))
# # # print(ray_list)
# # # slicing [start ,stop and step] syntax [start:stop:stop]
# # # print(ray_list[::-1])
# # # print(ray_list[:])
# # # print(ray_list[::2])
# # # print(ray_list[1::2])
# # # print(ray_list2)
# # # del ray_list[3]
# # # print(ray_list)
# # # print(reverse_ray)
# # # print(sorted(ray_list))
# # # print(ray_list.reverse())


# # # [b1,b2,b2a,b3,b4]
# # # fruits = ['apple','orange','grapes']
# # # print('apple')
# # print('apple,orange,grapes')
# # # print(fruits)
# # print('apple')
# # print('orange')
# # print('grapes')
# # # for fruit in fruits:
# #     print(fruit)

# # fav_color = input("What is your Favorate color : -\n ")
# # print(f"Your Favorate color is :- {fav_color} ")
# var  = 20
# print(f"this is a string : -  {var}")
# # print(f"Your Favorate color is : - {input("What is your favorate color : - ")}")



# Control Flow
# # this how actually the program is executing
# print("Hello")
# print("hey")
# print("Hello")
# if __name__=="__main__":
#     print("Very Good")

# if and else
# in python we are not having else if but we have elif 
# choice = input("You  want Coffee or Juice !! ")
# if choice=='coffee':
#     print("Sorry we do not have coffee")
# elif choice=="juice":
#     print("Yess Let's have some Juice")
# else:
#     print(f"Sorry ..... don't have {choice}")
# button = 'y'
# while button:
#     age = int(input("Enter your age : - "))
#     if age >18 and age <70:
#         print("THanks for voting")
#     elif age==18:
#         print("Sorry dear you need to wait for completing the 18")
#     else:
#         print("Invalid Age")
#     button =input("Do you want to continue : - ")
#     if button=='n':
#        break


# DSA
# Time Complexity and Space Complexity this is the main to study dsa
# why????? 1 mb perday * 365 days 365  1mb is 10 dirham = 22.710 * 365  inr = 70 lakh 2 

# Linear Search best case and average case and worst case ..
# for best case list = [2,1,3,4,5,6] find = 2  O(1)
# for worst case list = [1,3,4,5,6,2] find = 2  O(n)
# for average case O(n)
# low = 0 and high = len(list) = > low = 0 but high = mid -1
# list = [1,2,3,4,5,6] #= > list = [1,2,3]
# find = 2
# # flag = 0

# for index in range(0,len(list)):
#     if find == list[index]:
#         # flag  = 1
#         print(index)
#         break

# print(flag)
# for binary search the elements should be arranged in ascending or descending order
    
# two ways one is using loops and the other is using recursion 
    

# Binary Search in python


def binarySearch(array, x, low, high):
    # low = 0 and high = len(array)
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = (low+high)/2
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


for worst and average case O(logn) 
for best O(1) 