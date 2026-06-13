class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for stri in strs:
            result+=str(len(stri)) + '#' + stri
        
        return result

    def decode(self, s: str) -> List[str]:

        decoded = []

        if len(s) == 0:
            return []
        
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j].isdigit():
                j+=1
            
            length = int(s[i:j])
            i = j+1 # j must be hashtag here
            j = i + length

            decoded.append(s[i:j])

            i = j
        
        return decoded

