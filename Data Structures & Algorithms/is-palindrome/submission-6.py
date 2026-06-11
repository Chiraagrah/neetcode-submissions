class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        k = len(s) - 1
        while i<k:
            while i<k and not s[k].isalnum():
                k-=1
            while i<k and not s[i].isalnum():
                i+=1

            if s[i].lower() != s[k].lower():
                return False
            else:
                i+=1
                k-=1

        return True

