class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkpal(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1
        le = 0
        start, end = 0,0
        for x in range(len(s)):
            l1,r1 = checkpal(x,x)
            l2,r2 = checkpal(x-1,x)
            len1 = r1-l1+1
            len2 = r2-l2+1
            tstart,tend = (l1,r1) if len1>len2 else (l2,r2)
            if tend - tstart+1 > le:
                le = tend-tstart+1
                start,end = tstart,tend
        return s[start:end+1]