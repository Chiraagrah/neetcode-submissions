
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            if str(sorted(x)) not in dic:
                dic[str(sorted(x))] = [x]
            else:
                dic[str(sorted(x))].append(x)
        ans=[]
        for x in dic.values():
            ans.append(x)
        return ans