class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        x1 = 0
        for num in range(1, n):
            x1 ^= num
        
        x2 = nums[0]
        for i in range(1, n - 1):
            x2 ^= nums[i]
        
        return x1 ^ x2
