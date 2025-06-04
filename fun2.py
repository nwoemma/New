# def answer(nums):
#     seen ={}
#     for i in nums:
#         if i in seen:
#             return i
#         seen[i] = True
#     return -1

# def answer(num):
#     tracker = 1  # Start checking from 1
#     for i in num:
#         if i == tracker:
#             tracker += 1  # Move to the next expected number
#         else:
#             return tracker  # First missing number found
#     return tracker  # If all numbers are present, return the next expected number

# # Test case
# print(answer([2, 3, 4, 6]))  # Output: 1
# print(answer([1, 2, 3, 5]))  # Output: 4
# print(answer([1, 2, 3, 4]))  # Output: 5
# def ans(string):
#     tra = {}
#     for i in string:
#         if i not in tra:
#             tra[i] = 1
#         else:
#             tra[i] += 1
#     for i in string:
#         if tra[i] == 1:
#             return i 
        
# s = "aabbcddfe"
# print(ans(s))  # Output: 'c'

def answer(nums):
    largest = max(nums)
    second_largest = None
    for i in nums:
        if second_largest is None :
            second_largest = i if  i != largest else i > second_largest
    return second_largest if second_largest is not None else -1
# def __repr__(self):
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
        
#     def __repr__(emma):
        
# def largest(sentence):
#     largest = ""
#     for word in sentence.split():
#         if len(word) > len(largest):
#             largest = word
#     return largest
# a = "This is a test sentence"
# print(largest(a))  # Output: 'sentence'
# def vowels(string):
#     vowelss = "aeiou"
#     for i in string:
#         if i in vowelss:
#             return i
#     return -1
# a = "This is a test sentence"
# print(vowels(a)) 
# {} , [] ()

name = input('Enter your name: ')
age = 10
print ("My name is",name,'and i am',age,"years old")