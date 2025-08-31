# # def name():
# '''Function	Description
# abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	Returns the binary version of a number
# bool()	Returns the boolean value of the specified object
# bytearray()	Returns an array of bytes
# bytes()	Returns a bytes object
# callable()	Returns True if the specified object is callable, otherwise False
# chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method
# compile()	Returns the specified source as an object, ready to be executed
# complex()	Returns a complex number
# delattr()	Deletes the specified attribute (property or method) from the specified object
# dict()	Returns a dictionary (Array)
# dir()	Returns a list of the specified object's properties and methods
# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	Evaluates and executes an expression
# exec()	Executes the specified code (or object)
# filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
# format()	Formats a specified value
# frozenset()	Returns a frozenset object
# getattr()	Returns the value of the specified attribute (property or method)
# globals()	Returns the current global symbol table as a dictionary
# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system
# hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# issubclass()	Returns True if a specified class is a subclass of a specified object
# iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
# max()	Returns the largest item in an iterable
# memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable
# object()	Returns a new object
# oct()	Converts a number into an octal
# open()	Opens a file and returns a file object
# ord()	Convert an integer representing the Unicode of the specified character
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device
# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	Returns a readable version of an object
# reversed()	Returns a reversed iterator
# round()	Rounds a numbers
# set()	Returns a new set object
# setattr()	Sets an attribute (property/method) of an object
# slice()	Returns a slice object
# sorted()	Returns a sorted list
# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators
# '''
sentence = "I love python"
word =  [s for s in sentence.split()]
print(word)
    
    

# # def emma():
# #     name= input('Enter your name:  ')
# #     if name != "emma":
# #         print('sorry you are not the right person ')
# #     else:
# #         print(f'come in {name}')
# # emma()
# # for number in range(3, 61):
# #     print(number)
# # n = int(input("Enter a number: "))

# # Calculate the sum of numbers from 1 to n
# total_sum = sum(range(1, n + 1))

# Output the result
# print(f"The sum of all numbers from 1 to {n} is: {total_sum}")

# def even(num)
# for i in range(1,23):
#     if i%2 == 0:
#         print(i)
# def is_double(original, doubled):
#     match original, doubled:
#         case list() as orig, list() as dou if all(d == 2* o for o,d in  zip(orig, dou)):
#             return True
#         case _ :
#             return False
        
# sd = is_double([34,24],[68,68])
# print(sd)

# class Nums:
#     def __init__(self,original, doubled):
#         self.original = original
#         self.doubled = doubled

#     def is_checked(original,doubled):
#         match original, doubled:
#             case list() as orig, list() as dou if all(d == 2* o for o,d in  zip(orig, dou)):
#                 return True
#             case _ :
#                 return False
# num = Nums([34,34], [34,34])
# print(num.is_checked([68,68]))
# class Animals:
#     def __init__(self, name:str, sound:str):
#         self.name = name
#         self.sound  = sound
#     def make(self):
#         print(f'the sound made is {self.sound} and its name is {self.name} ')
        
# class Dog(Animals):
#     def __init__(self, name):
#         super().__init__(name)
        
#     def make
# def count_list(list_we):
#     count = {}
#     new_list = []
#     for i in list_we:
#         if i not in count:
#             new_list.append(i)
#             count[i] = 1
#     return new_list
# w = count_list([2,2,4,4,5])
# print(w)/
# def remove_dupl(input_num):
#     seen = {}
#     unique = []
#     for each in input_num:
#         if each not in seen:
#             unique.append(each)
#             seen[each] = True
#     return unique
# we = remove_dupl([3,5,45,45,12, 11])
# print(we)
# class Solution:
#     def search(self,nums:List[int], target:int) -> bool:
#         return True if target in nums else False
    
# # class Solution:
#     def deleteDuplicates(self, head:Optional[ListNode]) -> Optional[ListNode]:
#         if head == None:
#             return head
#         current = head
#         while current.next != None:
#             if current.val == current.next.val:
#                 current.next = current.next.next 
#             else:
#                 current = current.next
#         return head
# class Solution:
#     def deleteDuplicate(self, head:Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         current = dummy 
#         while current.next and current.next.next:
#             if current.next.val == current.next.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next 
#                 return dummy.next
# from typing import List   
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#        i = 0
#        for j in nums:
#            if i < 2:
                