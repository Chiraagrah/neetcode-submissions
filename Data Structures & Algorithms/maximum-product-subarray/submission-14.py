class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMin, currMax = 1,1
        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            temp = currMax * n
            currMax = max(temp, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            ans = max(ans, currMax)
        return ans

        
                

            