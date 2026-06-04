class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)
    
    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        result = []
        i = 0
        while i < len(s):
            next_iter = s.find("#", i)
            str_len = int(s[i:next_iter])
            start, end = next_iter+1, next_iter+1+str_len
            result.append(s[start:end])
            i = end

        return result