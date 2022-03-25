class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        numsSet = set(nums)
        hashSet = set()
        for num in range(1, n + 1):
            hashSet.add(num)
        for num in hashSet:
            if num not in numsSet:
                result.append(num)
                
        return result
