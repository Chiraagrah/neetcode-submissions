class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr,index):
            if index==len(nums):
                res.append(arr)
                return 
            backtrack(arr + [nums[index]],index+1)
            backtrack(arr,index+1)
        backtrack([],0)
        return res
            
                