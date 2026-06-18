class Solution:
    def isValid(self, s: str) -> bool:
        ds = {'(':')','{':'}','[':']'}
        de = {')','}',']'}
        stack =[]
        for x in s:
            if x in de:
                if not stack or ds[stack.pop()]!=x:
                    return False
            else:
                stack.append(x)
        return len(stack)==0
        