class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = min(cost[0]+cost[1],cost[1])
        for x in range(2,len(cost)):
            prev1,prev2 = min(prev1,prev2)+cost[x], prev1
            
        return min(prev1,prev2)