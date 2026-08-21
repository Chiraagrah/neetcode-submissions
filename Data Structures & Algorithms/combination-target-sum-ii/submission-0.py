class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start: int, path: List[int], leftOver: int):
            if leftOver == 0:
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > leftOver:
                    break

                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path, leftOver - nums[i])
                path.pop()

        backtrack(0, [], target)
        return res