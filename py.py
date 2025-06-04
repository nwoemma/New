# def que(s:str):
#     count = {}
#     for i in s:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     for k,v in count.items():
#         if v == 1:
#             return k
# def reverse(s:str):
#     words = s.split()
#     return " ".join(words[::-1])
def check(num:int) -> bool:
    return True if "1" in str(bin(num)[2:]) else False
from typing import List
def reverse_node_k_group(head:List[int], k:int) -> List[int]:
    if k == 1:
        return head
    res = []
    for i in range(0, len(head), k) :
        res += head[i:i+k][::-1]
    return res
