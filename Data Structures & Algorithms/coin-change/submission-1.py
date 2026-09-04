class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = [x for x in coins if x<=amount]
        if not coins:
            return -1
        coins.sort()
        ans = [float("inf")]*(amount+1)
        for amt in range(amount+1):
            for coin in coins:
                if coin==amt:
                    ans[amt] = 1
                    break
                elif amt-coin>0 and ans[amt-coin]!=float("inf"):
                    ans[amt] = min(ans[amt],1+ans[amt-coin])
        return -1 if ans[amt] == float("inf") else ans[amt]