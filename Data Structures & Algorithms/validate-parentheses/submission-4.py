class Solution:
    def isValid(self, s: str) -> bool:
        ds = {'(':')','{':'}','[':']'}
        de = {')','}',']'}
        stack =[]
        for x in s:
            if x in ds:
                stack.append(x)
            if x in de:
                if not stack or ds[stack[-1]]!=x:
                    return False
                stack.pop(-1)
        return len(stack)==0
        