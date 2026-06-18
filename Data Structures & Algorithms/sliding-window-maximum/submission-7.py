class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for x,y in enumerate(nums):
            while dq and nums[dq[-1]]<=y:
                dq.pop()
            dq.append(x)
            if dq[0]<=x-k:
                dq.popleft()
            if x>=k-1:
                ans.append(nums[dq[0]])
        return ans
            
