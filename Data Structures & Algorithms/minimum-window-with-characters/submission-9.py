from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        arr1 = Counter(t)
        set1= set(t)
        arr2= Counter([])
        start=0
        end = 0
        set2 = set()
        minle = float("inf")
        mins=-1
        minend = -1
        while end<len(s):
            if s[end] in arr1:
                arr2[s[end]]+=1
                if arr2[s[end]]==arr1[s[end]]:
                    set2.add(s[end])
            if set2==set1:
                while True:
                    if s[start] not in arr1:
                        start+=1
                        continue
                    if arr2[s[start]]>arr1[s[start]]:
                        arr2[s[start]]-=1
                        start+=1
                        continue
                    if arr2[s[start]]==arr1[s[start]]:
                        break
                if end-start+1<minle:
                    minle = end-start+1
                    mins = start
                    minend = end
                    arr2[s[start]]-=1
                    set2.remove(s[start])
                    start+=1
            end+=1
        if mins==-1:
            return ""
        return s[mins:minend+1]


            

        