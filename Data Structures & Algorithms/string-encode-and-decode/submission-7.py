class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        encoded = ""

        for s in strs:
            encoded += str(len(s)) + '#' + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        
        if len(s) == 0:
            return []

        
        decoded = []

        i = 0
        while i < len(s):
            j = i

            lengthDigit = ""
            while j < len(s) and s[j].isdigit():
                lengthDigit+=s[j]
                j+=1
            length = int(lengthDigit)

            i = j + 1
            j = i + length

            decoded.append(s[i:j])
            i = j
        
        return decoded
