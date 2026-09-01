class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0]*len(cost)
        ans[0] = cost[0]
        ans[1] = min(cost[0]+cost[1],cost[1])
        for x in range(2,len(cost)):
            ans[x] = min(ans[x-1],ans[x-2])+cost[x]
        return min(ans[len(cost)-1],ans[len(cost)-2])