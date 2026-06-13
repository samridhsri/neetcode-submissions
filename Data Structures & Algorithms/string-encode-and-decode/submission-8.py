class Solution:
    # How to remember this? -> Encode is length + # + word

    def encode(self, strs: List[str]) -> str:
        result = ""
        for element in strs:
            result += str(len(element)) + '#' + element
        
        return result

    def decode(self, s: str) -> List[str]:
        decoded = []

        if len(s) == 0:
            return []
        
        i = 0
        
        while(i < len(s)):
            j = i

            while j < len(s) and s[j].isdigit():
                j+=1
            
            length = int(s[i:j])
            i = j+1
            j = i + length

            decoded.append(s[i:j])

            i = j
        
        return decoded

