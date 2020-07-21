class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxarea = 0
        
        while (l<r):
            maxarea = max(maxarea, min(height[l],height[r]) * (r-l))
            
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
            
        return maxarea
