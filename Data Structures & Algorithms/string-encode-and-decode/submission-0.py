class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for x in strs:
            ans+= x + 'x%3'
        return ans
    def decode(self, s: List[str]) -> List[str]:
        temp=0
        ans=[]
        for x in range(len(s)):
            if s[x:x+3]=='x%3':
                ans.append(s[temp:x])
                temp=x+3
        return ans