class Solution:
    def twoSum(self, numbers: list[int], target: int) -> List[int]:
        numbers.sort()
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if sum_num == target:
                return [left+1, right+1]
            elif sum_num < target:
                left += 1
            elif sum_num > target:
                right -= 1
        return 
sol = Solution()
sol.twoSum([32,43,54.23], 32)