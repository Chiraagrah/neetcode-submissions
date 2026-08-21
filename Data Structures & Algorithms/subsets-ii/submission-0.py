class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(arr,index):
            res.append(arr.copy())

            for x in range(index,len(nums)):
                if x>index and nums[x]==nums[x-1]:
                    continue
                arr.append(nums[x])
                backtrack(arr,x+1)
                arr.pop()

        backtrack([],0)
        return res
        