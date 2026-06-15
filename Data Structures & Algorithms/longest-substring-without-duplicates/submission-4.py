class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        start=0
        end=1
        le = 1
        se = {s[start]}
        while end<len(s):
            if s[end] in se:
                le = max(le,end-start)
                while s[end] in se:
                    se.remove(s[start])
                    start+=1
            se.add(s[end])
            end+=1
        return max(le,end-start)
        