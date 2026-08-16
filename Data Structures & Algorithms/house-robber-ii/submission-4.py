class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        ans = [0] * (len(nums))
        ans[1] = nums[0]
        i = 2
        while i<=len(nums)-1:
            ans[i] = max(ans[i-1],ans[i-2]+nums[i-1])
            i+=1
        ans2 = [0]  * (len(nums)+1)
        i=2
        while i<=len(nums):
            ans2[i] = max(ans2[i-1],ans2[i-2]+nums[i-1])
            i+=1
        return max(ans[-1],ans2[-1])