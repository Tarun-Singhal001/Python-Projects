# print(list)
# import math
# lst = dir(math)
# print(lst)
# print(dir(math))

# list = [1, 2, [5, 6], 5, 8, ['a','g'], ['adbf', 'agjalkfj'], [ "alkf", "alkfj"] ]

"""
# This is a function to print number of elements in a list
def size_list(list_12):
    size = len(list_12)
    print("Size of list is : " , size)

size_list(list)
"""

"""
# Write a function to print the elements of a list

def elements_list(list_12):
    for item in list_12:
        print(item, end = " ")

elements_list(list)

"""

"""
# Write a function to write a factorial of a number n

def Fact(num):
    ans = 1
    for i in range(2,num+1):
        ans *= i
    print(ans, end = " 😁😁 ")


number = int(input("Enter a number: "))
Fact(number)
"""

"""
# WAF to convert USD to INR
def convertUtoI(money):
    print(round(money*85.57))
convertUtoI(10)
"""

"""
# WAF to convert INR to USD
def convertItoU(money):
    print(round(money/85.57))

convertItoU(8557)
"""

"""

def show(n):
    if(n < 0):
        return 0 
    print(n)
    show(n-1)

show(5)
"""

"""
# write a recursive function to calculate the sum of first natural numbers

def sum_of_natural(num):
    if num == 0:
        print(Sum)
        return 0
    sum = num + sum_of_natural(num-1)
        


sum_of_natural(20)
"""

"""
# Write a recursive function to print all the elements of a list

def print_list(list,index = 0):
    if(index == len(list)):
        return 0
    print(list[index], end = ' ')
    print_list(list,index+1)

list = [1, 2, [5, 6], 5, 8, ['a','g'], ['adbf', 'agjalkfj'], [ "alkf", "alkfj"] ]
print_list(list,3)
"""


