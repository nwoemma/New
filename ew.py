class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        cit_sorted = sorted(citations, reverse= True)
        for i in range(len(cit_sorted)):
            if cit_sorted[i] >= i + 1:
                h_index = i+1
            continue
        return h_index
class RandomizedSet:

    def __init__(self):
        self.val = None

    def insert(self, val: int) -> bool:
        if val is not None:
            return True
        else: return False
    def remove(self, val: int) -> bool:
        if val is None: return True
        else: return False

    def getRandom(self) -> int:
        pass

