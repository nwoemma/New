def reverse(s):
    i = len(s) - 1
    result = ""
    while i >= 0:
        result += s[i]
        i -= 1
    return result
reverse_str = reverse("strong")
print(f'the reverse of the word is: {reverse_str} ')
def reverse_second(s):
    word = ""
    for i in s:
        word += i
    return word

def reverse_third(s):
    return s[::-1]
s = "0P"
filtered_s = "".join(filter(str.isalpha, s))
filtered_s_strip = filtered_s.strip()
reverse_st = filtered_s_strip[::-1].lower()
print(reverse_st)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reorderList(self, head) -> None:
        if not head or head.next:
            return
    
    # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
        second_half = slow.next
        slow.next = None  # Split the list into two halves
        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
    
    # Now 'prev' is the head of the reversed second half
    
    # Step 3: Merge the two halves
        first_half, second_half = head, prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
a = ListNode()
print(a.reorderList([2,3,4,5]))