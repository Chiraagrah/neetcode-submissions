class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def checkPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        arr = []
        def backtrack(start):
            if start == len(s):
                result.append(arr.copy())
                return
            for window in range(start,len(s)):
                if checkPalindrome(start,window):
                    arr.append(s[start:window+1])
                    backtrack(window+1)
                    arr.pop()


        backtrack(0)
        return result
