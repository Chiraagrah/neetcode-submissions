class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        ds = {'(':')','{':'}','[':']'}
        de = {')','}',']'}
        stack =[]
        for x in s:
            if x in ds:
                stack.append(x)
            elif not stack or ds[stack.pop()]!=x:
                return False
        return len(stack)==0
        