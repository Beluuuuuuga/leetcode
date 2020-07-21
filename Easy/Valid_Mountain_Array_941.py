class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        num = len(A)
        if num < 3:
            return False
        
        i = 1
        while (i<num and A[i] > A[i-1]):
            i += 1
        
        if (i == 1 or i == num):
            return False
        
        while (i<num and A[i] < A[i-1]):
            i += 1
        
        return i == num
