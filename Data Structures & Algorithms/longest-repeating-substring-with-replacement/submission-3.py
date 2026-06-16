class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end=0
        ma = {}
        max_cnt = 0
        cn = 0
        le = 0
        while end<len(s):
            if s[end] not in ma:
                ma[s[end]]=1
            else:
                ma[s[end]]+=1
            if ma[s[end]]>max_cnt:
                max_cnt=ma[s[end]]
                max_char=s[end]
            if end-start+1-max_cnt>k:
                ma[s[start]]-=1
                max_cnt = max(ma.values())
                start+=1
            le = max(le,end-start+1)
            end+=1
        return le
        
