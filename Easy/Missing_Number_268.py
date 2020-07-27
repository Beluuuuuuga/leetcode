class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        currentSum = sum(nums)
        n = len(nums)
        indentedSum = n*(n+1)/2
        return int(indentedSum-currentSum)
