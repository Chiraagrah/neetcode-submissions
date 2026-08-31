class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*(n+1)
        if n<=2:
            return n
        one, two = 1, 2
        for _ in range(3, n + 1):
            current = one + two
            one = two
            two = current

        return two