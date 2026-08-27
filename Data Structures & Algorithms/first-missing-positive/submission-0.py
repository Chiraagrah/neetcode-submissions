class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(len(nums)):
            val = abs(nums[j])
            if 1<=val<=len(nums):
                cur = nums[val-1]
                if cur>0:
                    nums[val-1] = - nums[val-1]
                if cur == 0:
                    nums[val-1] = - (len(nums)+1)
        for i in range(1,len(nums)+1):
            if nums[i-1]>=0:
                return i
        return len(nums)+1