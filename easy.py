from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1
solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    
class Solution:
    def removeDuplicatesII(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
