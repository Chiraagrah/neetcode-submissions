class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start=0
        end=k
        loc = max(nums[start:end])
        ans = [loc]
        while end<len(nums):
            if nums[start]==loc:
                loc = max(nums[start+1:start+k+1])
                end+=1
                ans.append(loc)
                start+=1
                continue
            start+=1
            if nums[end]>loc:
                loc = nums[end]
            ans.append(loc)
            end+=1
        return ans
