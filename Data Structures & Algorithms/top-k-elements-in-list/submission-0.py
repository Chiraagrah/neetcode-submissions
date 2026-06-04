from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = [(i,j) for i,j in count.items()]
        ans.sort(key=lambda x:x[1],reverse=True)
        ans1=[]
        for x in range(k):
            ans1.append(ans[x][0])
        return ans1