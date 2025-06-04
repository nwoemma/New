# # In Python, there is a built-in filter function that operates similarly to JS's filter. 
# # For more information on how to use this function,
# # visit https://docs.python.org/3/library/functions.html#filter
# # The solution would work like the following:
# # get_even_numbers([2,4,5,6]) => [2,4,6]
# # solution
# # def get_even_numbers(numbers):
# #     return list(filter(lambda x: x % 2 == 0, numbers))
# # A = get_even_numbers([1,2,4,6,88])
# # print(A)

# # Take 2 strings s1 and s2 including only letters from a to z. 
# # Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming 
# # from s1 or s2.

# # Examples:
# # a = "xyaabbbccccdefww"
# # b = "xxxxyyyyabklmopq"
# # longest(a, b) -> "abcdefklmopqwxy"

# # a = "abcdefghijklmnopqrstuvwxyz"
# # longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
# # solution
# def longest(a1, a2):
#     return "".join(sorted(set(a1+a2)))\
# # There is a queue for the self-checkout tills at the supermarket. 
# # Your task is write a function to calculate the total time required for all the customers to check out!

# # input
# # customers: an array of positive integers representing the queue. Each integer represents a customer, 
# # and its value is the amount of time they require to check out.
# # n: a positive integer, the number of checkout tills.
# # output
# # The function should return an integer, the total time required.

# #solution
# # import heapq
# # def queue_time(customers, n):
# #     tills = [0] * n
# #     heapq.heapify(tills)
    
# #     # Process each customer
# #     for time in customers:
# #         # Assign the customer to the till with the smallest load (heapq.heappop)
# #         least_busy_till = heapq.heappop(tills)
        
# #         # Add the customer's time to that till
# #         least_busy_till += time
        
# #         # Push the updated load back into the heap
# #         heapq.heappush(tills, least_busy_till)
    
# #     # The total time required is the maximum value in the tills
# #     return max(tills)

# # Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
# def round_to_next5(n):
#     return n if n%5 == 0 else n +(5 - n%5)

# # Given the triangle of consecutive odd numbers:

# #              1
# #           3     5
# #        7     9    11
# #    13    15    17    19
# # 21    23    25    27    29
# # ...
# # Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# # 1 -->  1
# # 2 --> 3 + 5 = 8
# def row_sum_odd_numbers(n):
#     if n < 1:
#         raise ValueError("Row number must be a positive integer")


#     # Calculate the starting number in the nth row
#     start_num = (n * (n - 1)) // 2 + 1
    
#     # Calculate the ending number in the nth row
#     end_num = (n * (n + 1)) // 2
    
#     # Calculate the sum of the numbers from start_num to end_num
#     total_sum = sum(range(start_num, end_num + 1))
    
#     return 

# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i +1 ,len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return (i , j)
# # You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# # If there is no index that would make this happen, return -1.
# # For example:
# # Let's say you are given the array {1,2,3,4,3,2,1}:
# # Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# # Let's look at another one.
# # You are given the array {1,100,50,-51,1,1}:
# # Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# # Last one:
# # You are given the array {20,10,-80,10,10,15,35}
# # At index 0 the left side is {}
# # The right side is {10,-80,10,10,15,35}
# # They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# # Index 0 is the place where the left side and right side are equal.
# # Note: Please remember that in most languages the index of an array starts at 0
# # Input
# # An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
# # Output
# # The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.
# # Note
# # If you are given an array with multiple answers, return the lowest correct index.          
# def find_even_index(arr):
#     total = sum(arr)
#     left = 0
#     for i, num in enumerate(arr):
#         right = total - left - num
#         if left == right:
#             return i
#         left += num
#     return -1
# '''
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. 
# When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
# The left side letters and their power:
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!
# def alphabet_war(fight):
#     left_side = {'w':4,'p':3,'b':2,'s':1}
#     right_side = {'m':4,'q':3,'d':2,'z':1}
    
#     left_score = sum(left_side[letter] for letter in fight if letter in left_side)
#     right_score = sum(right_side[letter] for letter in fight if letter in right_side)
    
#     if left_score > right_score:
#         return "Left side wins!"
#     elif right_score > left_score:
#         return "Right side wins!"
#     else:
#         return "Let's fight again!"
# '''
# '''
# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.   
# '''
    

# def decrypt(text, n):
#     if not text or n <= 0:
#         return text
    
#     # Repeat the decryption process N times
#     for _ in range(n):
#         mid = len(text) // 2
#         odd_chars = text[:mid]
#         even_chars = text[mid:]
        
#         # Rebuild the string by interleaving even and odd characters
#         decrypted_text = []
#         for i in range(mid):
#             if i < len(even_chars):
#                 decrypted_text.append(even_chars[i])  # Add even-indexed characters first
#             if i < len(odd_chars):
#                 decrypted_text.append(odd_chars[i])  # Add odd-indexed characters second
#         # If the length of text is odd, the last even character may remain unadded
#         if len(even_chars) > mid:
#             decrypted_text.append(even_chars[-1])
#         text = ''.join(decrypted_text)  # Update the text after each iteration
#     return text


# def encrypt(text, n):
#     if not text or n < 0:
#         return text
#     for _ in range(n):
#         odd_chars = ''.join([text[i] for i in range(1, len(text), 2)])
#         even_chars = ''.join([text[i] for i in range(0, len(text), 2)])
#         text = odd_chars + even_chars 
#     return text

# # wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
def wave(s):
    result = []
    for i in range(len(s)):
        if s[i].isalpha():  # Only process alphabetic characters
            result.append(s[:i] + s[i].upper() + s[i+1:])  # Capitalize the letter at index i
    return result
a = wave('adetr')
print(a)
"""
As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between
the other two elements.
The input to the function will be an array of three distinct numbers (Haskell: a tuple).
For example:
gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
Another example (just to make sure it is clear)
gimme([5, 10, 14]) => 1
10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.
"""
def gimme(input_array):
    # Check if the first element is the middle element
    if (input_array[0] > input_array[1] and input_array[0] < input_array[2]) or \
       (input_array[0] < input_array[1] and input_array[0] > input_array[2]):
        return 0
    # Check if the second element is the middle element
    elif (input_array[1] > input_array[0] and input_array[1] < input_array[2]) or \
         (input_array[1] < input_array[0] and input_array[1] > input_array[2]):
        return 1
    # If neither of the above, then the third element must be the middle one
    else:
        return 2