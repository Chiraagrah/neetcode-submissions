class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*(n+1)
        if n<=2:
            return n
        arr[1] = 1
        arr[2] = 2
        for x in range(3,n+1):
            arr[x] = arr[x-1] + arr[x-2]
        return arr[n]