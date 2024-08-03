# function 
# def ray(name,subject):
#     print(f'THe Name is {name} and the Subject is {subject}')

# ray("shaiban","computer science")

# def voting(age):
#     if age >18 and age<80:
#         print("Thanks for voting")
#         return True
#     elif age==18:
#         print("Sorry You need to complete 18 ")
#     elif age<10 and age>5:
#         print("Sorry you need to wait ..")
#     else:
#         print("Invalid Age")
#     return False

# result  = voting(8)
# print(result)


# def __str__(name,subject):
#     a = name + subject
#     print(a)
# print(20,30)

# print("Ray")
# vote_result_1 = voting(18)
# vote_result_2 = voting(60)
# print(vote_result_1)
# print(vote_result_2)


# Type Conversion 

# num1 = float(input("Enter a Num1 : - "))
# num2 = int(input("Enter num2 : - "))
# result = num1+num2
# print(result)
# list = ['apple','mangoo','grapes','kiwi']
# for element in list:
#     print(element,sep="-->>")

# pass in python
# if 2<10:
#     pass
    
# scope what is scope?

# class Ray():
#     name = "Raiyan"
#     subject = 'cs'
#     def speak(name):
#         likes = 'Studying'
#         print(f'{name} is speaking , likes {likes}')
#     speak(name)

# Inheritance 

#-->>  A class is a blueprint and you can often make multiple objects of the class
# class Animal:
#     No_of_hands = 2
#     No_of_legs = 2
#     def walk(self):
#         print("Animal is walking")
#     def eat(self):
#         print("Animal is Eating")

# dog = Animal()
# dog.eat()
# dog.walk()

# cat = Animal()
# cat.eat()
# cat.walk()

# monkey = Animal()
# monkey.eat()
# monkey.walk()


class parent:
    car = 'This is Car BMW'

class child(parent):
    toy_car = 'This is a toy Car Supra'


Ray = child()
Ray_Mom = parent()
print(Ray_Mom.car)
print(Ray_Mom.toy_car)
print(Ray.toy_car)
print(Ray.car)