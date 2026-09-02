class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkpal(l,r):
            count = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        count = 0
        for x in range(len(s)):
            count += checkpal(x,x) + checkpal(x-1,x)
        return count