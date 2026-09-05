class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        prefix = suffix = 1

        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]  # ~i traverses backwards: n - 1 - i
            ans = max(ans, prefix, suffix)

        return ans

        
                

            