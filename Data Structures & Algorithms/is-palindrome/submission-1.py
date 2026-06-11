class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start <= end:
            while start<len(s) and not s[start].isalnum():
                start+=1
            while end>=0 and not s[end].isalnum() :
                end-=1
            if start>end:
                break
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True
        