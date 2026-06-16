from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        cnt1 = [0]*26
        cnt2 = [0]*26
        for x in range(len(s1)):
            cnt1[ord(s1[x])-ord('a')]+=1
            cnt2[ord(s2[x])-ord('a')]+=1
        if cnt1==cnt2:
            return True
        
        for x in range(len(s1),len(s2)):
            cnt2[ord(s2[x-len(s1)])-ord('a')]-=1
            cnt2[ord(s2[x])-ord('a')]+=1
            if cnt1==cnt2:
                return True
        return False
        
        

