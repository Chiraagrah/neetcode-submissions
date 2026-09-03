class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            # Single-digit take
            ans = dfs(i + 1)

            # Two-digit take (valid between 10 and 26)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                ans += dfs(i + 2)

            memo[i] = ans
            return ans

        return dfs(0)