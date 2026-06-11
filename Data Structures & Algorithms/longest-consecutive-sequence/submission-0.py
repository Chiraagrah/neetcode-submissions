class Solution:
    def che(self, se, x, start):
        if x+1 not in se:
            return start
        else:
            return self.che(se,x+1,start+1)
    def longestConsecutive(self, nums: List[int]) -> int:
        se = set(nums)
        ma = 0
        for x in nums:
            if x-1 in se:
                continue
            else:
                sta=1
                sta = self.che(se,x,sta)
                if sta>ma:
                    ma=sta
        return ma

    