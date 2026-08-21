class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr,index):
            if index==len(nums):
                res.append(arr)
                return 
            if not arr:
                temp = [nums[index]]
            else:
                temp = arr + [nums[index]]
            backtrack(temp,index+1)
            backtrack(arr,index+1)
        backtrack([],0)
        return res
            
                