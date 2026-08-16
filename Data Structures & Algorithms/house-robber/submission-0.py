class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0]*(len(nums)+1)
        i = 2
        ans[1] = nums[0]
        while i<=len(nums):
            ans[i] = max(ans[i-1],ans[i-2]+nums[i-1],ans[i-3]+nums[i-1])
            i+=1
        return ans[-1]