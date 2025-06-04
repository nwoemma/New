# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         def splitlist(head):
#             slow, fast = head, head
#             mid = None
#             while fast and fast.next:
#                 mid = slow
#                 slow = slow.next
#                 fast = fast.next.next
#             mid.next = None
#             return head, slow
#         def mergelist(l1,l2):
#             dummy = ListNode(0)
#             current = dummy
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     current.next = l1
#                     l1 = l1.next
#                 else:
#                     current.next = l2
#                     l2 = l2.next
#                 current = current.next
#             current.next = l1 if l1 else l2
#             return dummy.next
#         left, right = splitlist(head)
#         left = self.sortList(left)
#         right = self.sortList(right)
#         return mergelist(left,right
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            
            
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            else: 
                right -= 1
        return "".join(s)
    