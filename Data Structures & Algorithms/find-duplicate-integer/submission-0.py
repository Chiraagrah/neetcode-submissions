class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        se = set()
        for x in nums:
            if x in se:
                return x
            else:
                se.add(x)
        
        