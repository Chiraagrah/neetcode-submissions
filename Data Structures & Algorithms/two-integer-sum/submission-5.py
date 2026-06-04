class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b=sorted(nums)
        i,j=0,len(nums)-1
        while i<j:
            temp = b[i]+b[j]
            if temp==target:
                break
            if temp<target:
                i+=1
            if temp>target:
                j-=1
        ans=[]
        for x in range(len(nums)):
            if b[i]==nums[x] and i!=-1:
                ans.append(x)
                i=-1
            elif b[j]==nums[x] and j!=-1:
                ans.append(x)
                j=-1
            if i==-1 and j==-1:
                break
        return sorted(ans)


       