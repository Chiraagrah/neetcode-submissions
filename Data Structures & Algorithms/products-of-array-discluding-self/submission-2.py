class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=len(nums)-1
        left=[1]*len(nums)
        right=[1]*len(nums)
        le=1
        ri=1
        while a>=0:
            left[len(nums)-1-a]=le
            le*=nums[len(nums)-1-a]
            right[a]=ri
            ri*=nums[a]
            a-=1
        a=0
        while a<len(nums):
            left[a]=left[a]*right[a]
            a+=1
        return left

            
        