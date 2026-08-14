class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        for ch in s:
            ch = ch.lower()
            freq[ord(ch) - ord('a')] += 1
        
        for ch in t:
            ch = ch.lower()
            freq[ord(ch)-ord('a')]-=1
        
        for c in freq:
            if c!=0:
                return False
        
        return True