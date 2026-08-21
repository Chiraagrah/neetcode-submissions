class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index,current_combo,remaining):

            if remaining == 0:
                res.append(current_combo.copy())
                return
            if remaining < 0 or index >= len(nums):
                return
            
            current_combo.append(nums[index])
            backtrack(index, current_combo, remaining - nums[index])
            current_combo.pop() 
            
            backtrack(index + 1, current_combo, remaining)

        backtrack(0, [], target)
        return res