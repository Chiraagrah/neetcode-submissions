class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ma = 0
        for x in nums:
            if x-1 in nums:
                continue
            else:
                sta=1
                temp=x+1
                while temp in nums:
                    sta+=1
                    temp+=1
                if sta>ma:
                    ma=sta
        return ma

    