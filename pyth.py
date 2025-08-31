# class some_code:
    # def start(name):
# from typing import List
# class Solution:
#     def search(self, nums:List[int], target:int)->int:
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

# def find_majority(arr):
#     count = {}
#     for num in arr:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#     max_num = max(count, key=count.get)
#     return max_num
# A = [1,2,2,2,2,2,3,4,3,3,5,2,1,3]
# print(find_majority(A))

# def even_nums(nums:list):
#     new_list = []
#     for i in nums:
#         if i % 2== 0:
#             new_list.append(i)
#     return new_list

# A = [1,2,2,2,2,2,3,4,3,3,5,2,1,3]
# print(even_nums(A))
# def hIndex(self, citations: List[int]) -> int:
# def pairs(numbers:list, target:int) -> list:
#     nums = [] 
#     seen = {}
#     for num in numbers:
#         seen[num] = True
#         compliment = target - num
#         if compliment in seen:
#             nums.append((compliment, num))
#     return nums
# print(pairs([2,4,3,5,7,8,9],10))

# def is_palindrome(s:str) -> bool:
#     return True if s == s[::-1] else False
# def is_anagram(first, second):
#     return sorted(first) == sorted(second)
# print(is_anagram("listen", "silent"))
# def most(nums:list):
#     count = {}
#     for num in nums:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#     return max(count, key=count.get)
# def ae(s:str):
#     i = 1
#     while i < len(s):
#         if
        
# def qw(s:list):
#     count = {}
#     for i in s:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     for key, val in count.items():
#         if val == 1:
#             return key
# def qwe(s:list):
#     count = {}
#     for i in s:
#         if i in count:
#             count[i] +=1
#         else:
#             count[i] = 1
#     return max(count, key=count.get)

# def qeq(s:str):
#     count = {}
#     for i in s: 
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     for key,val in count.items():
#         if val == 1:
#             return key
    
    
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
        
    # def __repr__(self):
    #     return f"Person(name={self.__name}, age={self._age})"
    
    # def __str__(self):
    #     return f"{self.__name} is {self._age} years old."
    
    # def ema(self):
    #     return self.__name
    
# s = Person("John", 30)
# print(s.ema())
       
    
    
    
# def first_unique(string):
#     count = {}
#     for i in string:
#         if i in count:
#             count[string] += 1
#         else:
#             count[string] = 1
#     for key, val in count.items:
#         if val == 1:
#             return key
            
            
# print(first_unique("aabbccddeefg")  )

# def filter_even(nums):
#     new_nums = []
#     for num in nums:
#         if num % 2 == 0:
#             new_nums.append(num)
#     return new_nums

# w = filter_even([1,2,3,4,5,6])
# print(w)
            
# def count_vowels(string):
#     vowels = 'aeiou'
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1
#     return count

# w = count_vowels("hello world")
# print(w)
        
# def has_pair_with_sum(nums,target):
#     seen = set()
#     for num in nums:
#         comp = target - num
#         if comp in seen:
#             return True
#         seen.add(num)
#     return False
            

# q= has_pair_with_sum([10,15,3,7],17)
# print(q)
# def remove_duplicate(numbers):
#     seen = set(numbers)
#     for num in numbers:
#         if num not in seen:
#             seen.add(num)
#         return list(seen)
    
        
# s= [5,5,5,5]
# print(remove_duplicate(s))


# def top_k_frequent(nums, k):
#     count = {}
#     for item in nums:
#         if item in count:
#             count[item] += 1
#         else:
#             count[item]  = 1
#     filtered = [key for key, val in count.items() if val >=k]   
#     return filtered
        
# e = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
# print(e)

# def longest_consecutive_sequence(numbers:list):
#     # organized = sorted(numbers)
#     numbers.sort()
#     n = 0
#     while n <= len(numbers):
#         diff = numbers[n] - numbers[n-1]
#         if diff != 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.replac

# def counting(numbers):
#     seen = {}
#     for num in numbers:
#         if num in seen:
#             seen[num] += 1
#         else:
#             seen[num] = 1
#     return seen
# d = counting([1,2,2,3,1,1])
# print(d)

# def sec_max_num(nums):
#     print(nums)
#     largest = nums[0]
#     second_largest = nums[1]
#     for num in nums:
#         if largest < num:
#            largest = num
#            nums.remove(largest)
#         if second_largest < num:
#             second_largest = num
#     return second_largest 
# d = [1,2,3,4,5]
# print(sec_max_num(d))
        
# def algo_opti(nums:list, k:int) -> int : 
#     unique = []          
    
# d = [4,1,2,2,5,5,7,7]
# print(algo_opti(d,3))

# def reverse_str(sentence=str):
#     word =  [s for s in sentence.split()]
#     reverse_word = word[::-1]
#     return " ".join(reverse_word)

# sentence = "I love Python"
# print(reverse_str(sentence))

# word = [1,2,4,6]
# print(word[::-1])
# from typing import List
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums = nums1 + nums2
#         nums_sorted = sorted(nums)
#         n = len(nums_sorted)  
#         if n % 2 == 1:    
#             med = nums_sorted[n //2]
#         else:
#             med =(nums_sorted[(n //2)-1] + nums_sorted[n //2])/2
#         return med
            
            

# nums1 = [1,2]
# nums2= [3,4]

# s =Solution()
# print(s.findMedianSortedArrays(nums1, nums2))