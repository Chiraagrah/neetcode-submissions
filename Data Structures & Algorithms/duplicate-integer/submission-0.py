class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        if not nums:
            return False
        for x in nums:
            if x not in a:
                a.add(x)
            else:
                return True
        return False