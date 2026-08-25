class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parentconnect = {i:i for i in range(1,len(edges)+1)}
        def canConnect(l,h):
            if parentconnect[l] == parentconnect[h]:
                return False
            leftp = max(parentconnect[l],parentconnect[h])
            parent = min(parentconnect[l],parentconnect[h])
            for c, p in parentconnect.items():
                if p == leftp :
                    parentconnect[c]=parent
            return True
        for l,h in edges:
            if not canConnect(l,h):
                return [l,h]
        