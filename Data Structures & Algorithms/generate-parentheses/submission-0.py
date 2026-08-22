class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(st, count_op,count_clos):
            if count_clos==0 and count_op== 0:
                res.append(st)
                return
            elif count_op==0:
                st += ")"
                backtrack(st,0,count_clos-1)
            else:
                backtrack(st+ "(", count_op-1,count_clos+1)
                if count_clos>0:
                    backtrack(st+")",count_op,count_clos-1)
        backtrack("",n,0)
        return res