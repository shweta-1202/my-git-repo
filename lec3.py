# dictionary comprehension
# sqr = {x:x*x for x in range(6)}    #(key:value)
# print(sqr)

# cube in 1 to 10
# a = {x:x**3 for x in range(1,11,2)}
# print(a)

# dict = {i:i**3 for i in range(1,11) if i!=7}
# print(dict.items())



# list comprehension
# list = [x for x in range(2,9) if x!=5]
# print(list)

# y = 14
# a = [x*y for x in range(101,122)]
# print(a)

# even numbers from 2 to 28
# a = [x for x in range(2,29) if (x%2==0)]
# print(a)

# user = int(input('message'))
# print(user)

# list = []
# n = int(input('enter the length of list '))
# for i in range(n):
#     user = int(input(f'{i+1} value '))
#     list.append(user)
# print(list)

# function
# def a(x,y):
#define function_name(PARAMETER)
#     c=x*y    #first priority
#     return c
#     c=x+y    #it will not go here
# p=a(2,3)
# print(p)
#print =prints the value
#return= does not return the value but performs task


# def add():
#     s=0
#     for i in range (5):
#         a=int(input())
#         s+=a
#     print(s)
#     return s
# add()

# print(abs(9.7777))

# def a(name,roll_no):
#     print(f'{name} is roll_no {roll_no}')
# p=a(roll_no=92,name='krutika')
# print(p)

# def age():
#     s=0
#     for i in range (6):
#         a=int(input())
#         s+=a
#     print(s)
#     return s
# add()


# calculate avg of age without function
# list = []
# n = int(input('enter the length of list '))
# for i in range(n):
#     user = int(input(f'{i+1} student '))
#     list.append(user)  
# s = sum(list)
# print(s)
# a = s/n
# print(a)

# calculate avg of age with function
# def avg():
#     list = []
#     n = int(input('enter the length of list '))
#     for i in range(n):
#         user = int(input(f'{i+1} student '))
#         list.append(user)  
#     s = sum(list)
#     print(s)
#     a = s/n
#     return a
# print(avg())
    

# arbitrary arguements, *args: when we dont know how many args are there
#define function (*argument):
# def age(*b):
#     print(b)
#     print(type(b))
# age([2,5,6,7])


# arbitrary keyword arguements, **kwargs:
# def age(**b):
#     print(b)
#     print(type(b))
# age(a=2,b=5,c=6,d=7)


# def add(x,y):
#     c=x+y
#     print(c)


# add = lambda x,y : x+y
# #function name = lambda parameters : operation
# p=add(1,2)
# print(p)

# sub = lambda x,y : x-y
# #function name = lambda parameters : operation
# p=sub(3,2)
# print(p)

# mul = lambda x,y : x*y
# #function name = lambda parameters : operation
# p=mul(1,2)
# print(p)

# div = lambda x,y : x/y
# #function name = lambda parameters : operation
# p=div(20,4)
# print(p)

# sqr = lambda x : x*x
# #function name = lambda parameters : operation
# p=sqr(5)
# print(p)
