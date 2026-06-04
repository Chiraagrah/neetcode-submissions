
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            if str(sorted(x)) not in dic:
                dic[str(sorted(x))] = [x]
            else:
                dic[str(sorted(x))].append(x)
            
        return list(dic.values())