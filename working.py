# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from typing import Optional
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if not headA or not headB:
#             return None

#         pointer_1, pointer_2 = headA, headB
#         while pointer_1 != pointer_2:
#             pointer_1 = pointer_1.next if pointer_1 else headB
#             pointer_2 = pointer_2.next if pointer_2 else headA

#         return pointer_1
# def func(start, end):
#     return [i for i in range(start, end+1)]
# e = func(23,43)
# print(e)

# for i in range(1,32+1):
#     print(i)
# total = 0
# num = 190
# for i in range(num):
#     total += num
# print(total)

# def sum_numbers(num):
#     total = 0
#     for i in range(num):
#         total = num + total
#     return total
# print(sum_numbers(190))
# total = 0
# i = 0
# num = 12
# while i <= num:
#     total = total + i
#     i += 1
# print(total)
# def sum_num(num):
#     total = 0
#     i = 0
#     while i <= num:
#         total += i
#         i += 1
#     return total
# print(sum_num(345))
# a = 1
def asqws(a,b,flag):
    if a > 0 and b < 0 and flag == False:
        return True
    elif a == b <= 0 and flag == True:
        return True
    else:
        return False
    
print(asqws(23,-55, False))