class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = 0
        for n in nums:
            dic[n] += 1
        newdic = sorted(dic.items(), key=lambda x:x[1])
        return newdic[0][0]
