class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        booleanArr = [False for _ in range(len(nums))]
        def backtrack(boolarr,arr):
            count = 0
            for x in range(len(nums)):
                if not boolarr[x]:
                    arr.append(nums[x])
                    boolarr[x]= True
                    backtrack(boolarr,arr)
                    boolarr[x]=False
                    arr.pop()
                if boolarr[x]:
                    count+=1
                    continue
            if count == len(boolarr):
                res.append(arr.copy())
        backtrack(booleanArr,[])
        return res

