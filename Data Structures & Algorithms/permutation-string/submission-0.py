from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        cnt = {}
        for x in s1:
            if x not in cnt:
                cnt[x]=1
            else:
                cnt[x]+=1
        start=0
        end= 0
        crnt = {}
        while end<len(s2):
            if s2[end] not in crnt:
                crnt[s2[end]]=1
            else:
                crnt[s2[end]]+=1
            if end-start+1 == len(s1) and crnt==cnt:
                return True   
            if end-start+1>=len(s1):
                crnt[s2[start]]-=1
                if crnt[s2[start]]==0:
                    del crnt[s2[start]]
                start+=1
            end+=1
        return False
        
        

